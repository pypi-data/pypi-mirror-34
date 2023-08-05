from . import control

from .logger import plog

############## Rendguard options #####################

# Minimum number of hops we have to see before applying use stat checks
REND_USE_GLOBAL_START_COUNT = 100

# Number of hops to scale counts down by two at
REND_USE_SCALE_AT_COUNT = 1000

# Minimum number of times a relay has to be used before we check it for
# overuse
REND_USE_RELAY_START_COUNT = 10

# How many times more than its bandwidth must a relay be used?
REND_USE_MAX_USE_TO_BW_RATIO = 2.0

# Should we close circuits on rend point overuse?
REND_USE_CLOSE_CIRCUITS_ON_OVERUSE = True

class RendUseCount:
  def __init__(self, idhex, weight):
    self.idhex = idhex
    self.used = 0
    self.weight = weight

class RendGuard:
  def __init__(self):
    self.use_counts = {}
    self.total_use_counts = 0
    self.pickle_revision = 1

  def valid_rend_use(self, r):
    if r not in self.use_counts:
      plog("NOTICE", "Relay "+r+" is not in our consensus, but someone is using it!")
      self.use_counts[r] = RendUseCount(r, 0)

    self.use_counts[r].used += 1
    self.total_use_counts += 1.0

    # TODO: Can we base this check on statistical confidence intervals?
    if self.total_use_counts > REND_USE_GLOBAL_START_COUNT and \
       self.use_counts[r].used >= REND_USE_RELAY_START_COUNT:
      plog("INFO", "Relay "+r+" used "+str(self.use_counts[r].used)+
                  " times out of "+str(int(self.total_use_counts)))

      if self.use_counts[r].used/self.total_use_counts > \
         self.use_counts[r].weight*REND_USE_MAX_USE_TO_BW_RATIO:
        plog("WARN", "Relay "+r+" used "+str(self.use_counts[r].used)+
                     " times out of "+str(int(self.total_use_counts))+
                     ". This is above its weight of "+
                     str(self.use_counts[r].weight))
        return 0
    return 1

  def xfer_use_counts(self, node_gen):
    old_counts = self.use_counts
    self.use_counts = {}
    for r in node_gen.sorted_r:
       self.use_counts[r.fingerprint] = RendUseCount(r.fingerprint, 0)

    i = 0
    rlen = len(node_gen.rstr_routers)
    while i < rlen:
      r = node_gen.rstr_routers[i]
      self.use_counts[r.fingerprint].weight = \
         node_gen.node_weights[i]/node_gen.weight_total
      i+=1

    # Periodically we divide counts by two, to avoid overcounting
    # high-uptime relays vs old ones
    for r in old_counts:
      if r not in self.use_counts: continue
      if self.total_use_counts > REND_USE_SCALE_AT_COUNT:
        self.use_counts[r].used = old_counts[r].used/2
      else:
        self.use_counts[r].used = old_counts[r].used

    self.total_use_counts = sum(map(lambda x: self.use_counts[x].used,
                                    self.use_counts))
    self.total_use_counts = float(self.total_use_counts)

  def circ_event(self, controller, event):
    if event.status == "BUILT" and event.purpose == "HS_SERVICE_REND":
      if not self.valid_rend_use(event.path[-1][0]):
        if REND_USE_CLOSE_CIRCUITS_ON_OVERUSE:
           control.try_close_circuit(controller, event.id)

    plog("DEBUG", event.raw_content())
