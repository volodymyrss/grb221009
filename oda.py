from odafunction import LocalPythonFunction
from odafunction.func.urifunc import URIPythonFunction, URIipynbFunction    
import odafunction.logs
from fcat import Cat       

odafunction.logs.app_logging.setup()    

__all__ = ["fd", "fc", "results", "r2560", "total_3p", "lateobs"]


fd = Cat(asdict=True)  


fc = Cat()

fc.add("cites", 
        URIPythonFunction("file:///home/savchenk/grb221009/cite_semantic.py::gen"))


results = fc.grbbase(focus_obs_name="total_3p")['data']
total_3p = results

eventrate = fd.eventrate

r2560 = fc.grbbase(focus_obs_name="r2560")['data']

r = fc.grbbase(focus_obs_name="late")
lateobs = r['data']
