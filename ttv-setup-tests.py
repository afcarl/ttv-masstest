import rebound


	def bisect(sim,t1,t2):
	    tm = (t1+t2)/2.
	    if t2-t1<(5.0e-7):
	        return tm
	    sim.integrate(tm)
	    if sim.particles[0].y>0.:
	        t2 = tm
	        return bisect(sim,t1,t2)
	    else:
	        t1 = tm
	        return bisect(sim,t1,t2)


sim = rebound.Simulation()
sim.add(m=1.)
planet1_params = {"a":0.5, "m":0.0002}
sim.add(primary=sim.particles[0], **planet1_params)
sim.move_to_com()
sim.integrate(1.)

transits = 3
D = 0.
D_previous = 0.
time = 0.
time_previous = 0.
while(transits > 0):
	sim.step()
	D = 
	time = sim.t
	if(D>0 and D_previous<0):
		transit_time = bisect(sim, time, time_previous)