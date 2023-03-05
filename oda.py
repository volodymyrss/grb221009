from odafunction import LocalPythonFunction
from odafunction.func.urifunc import URIPythonFunction, URIipynbFunction    
import odafunction.logs
from fcat import Cat       

odafunction.logs.app_logging.setup()    

__all__ = ["fd", "fc", "results", "r2560", "total_3p", "lateobs", 
           "r2558",  "r25589", "r2559", "ag", "ag_fit",
           "rings", "iil", 
           "literature", "known_facts"]


fd = Cat(asdict=True)  


fc = Cat()

fc.add("cites", 
        URIPythonFunction("file:///home/savchenk/grb221009/cite_semantic.py::gen"))


results = fc.grbbase(focus_obs_name="total_3p")['data']
total_3p = results

eventrate = fd.eventrate

r2558 = fc.grbbase(focus_obs_name="r2558")['data']
r2559 = fc.grbbase(focus_obs_name="r2559")['data']
r25589 = fc.grbbase(focus_obs_name="r25589")['data']
r2560 = fc.grbbase(focus_obs_name="r2560")['data']

r = fc.grbbase(focus_obs_name="late")
lateobs = r['data']

fd.positrons["ul_positrons_msun"]

ag = fc.afterglow(nsampler=3000)
#ag = fc.afterglow(nsampler=30)
#ag = fc.afterglow(nsampler=3000)
ag_fit = ag['ag_fit']
rings = ag['rings']

iil = fc.iilight()

literature = fc.literature()
known_facts = literature['facts']

#stat_err_plus
