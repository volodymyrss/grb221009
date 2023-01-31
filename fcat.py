import glob
import inspect
import os
import base64
import logging

from odafunction.executors import default_execute_to_value
from odafunction.func.urifunc import URIPythonFunction, URIipynbFunction, URIValue
from odafunction.catalogviews import FunctionCatalogKeyedLocalValuedAttrs


logger = logging.getLogger(__name__)


class Cat(FunctionCatalogKeyedLocalValuedAttrs):
    def __init__(self, asdict=False, pattern="../*.ipynb") -> None:
        super().__init__()
    
        self.asdict = asdict

        for fn in glob.glob(pattern):
            self.add(os.path.basename(fn).replace(".ipynb", ""), 
                    URIipynbFunction.from_generic_uri("file://" + os.path.abspath(fn)))


    def extract_images(self, fn_prefix, r, prefix):
        if isinstance(r, dict):

            logger.info(f"\033[31mrunning extract images\033[0m %s %s", fn_prefix, repr(r)[:200])
            image_dict = {}

            for c in r['output_nb']['cells']:
                for output in c.get('outputs', []):
                    if img_b64:=output.get('data', {}).get('image/png', None):                                                            
                        logger.info(f"*found image >>>*")
                        image_dict[f'img_{len(image_dict)}'] = img_b64

            for k, v in r['output_values'].items():
                if k.endswith("_content"):                                                            
                    logger.info(f"[red]found image >>>[/] %s", k)
                    image_dict[k.replace("_content", "")] = v

            
            for k in image_dict:
                logger.info(f"[red] summary found image >>>[/] %s", k)
                        

            def savefig(name, fn):
                os.makedirs(os.path.dirname(fn), exist_ok=True)
                logger.info(f"\033[31mcell outputs image stored to >>>\033[0m %s", fn)
                with open(fn, "wb") as f:                        
                    f.write(base64.b64decode(image_dict[name]))
                
                return f"{prefix}/{name}".replace("_", "\_")

            r['output_values']['savefig'] = savefig



    def __getattr__(self, __name: str) -> callable:
        if __name in self.catalog:
            func = self.catalog[__name]

            fn_prefix = "figs/" + __name

            logger.info("\033[31mfunc.signature: %s\033[0m", func.signature)

            if self.asdict:
                r = default_execute_to_value(func, cached=True, valueclass=URIValue)
                logger.info("default_execute_to_value returns %s", repr(r)[:200])
                self.extract_images(fn_prefix, r, func.uri)
                if __name in r['output_values']:
                    r = r['output_values'][__name]
                else:
                    r = r['output_values']
            else:
                def f(*args, **kwds):
                    f0 = func(*args, **kwds)
                    v = default_execute_to_value(f0, cached=True, valueclass=URIValue)
                    if isinstance(f0, (URIipynbFunction, URIPythonFunction)):
                        print("extracting images")
                        self.extract_images(fn_prefix, v, __name)                        
                    else:
                        print("NOT extracting images for", f0)
                    
                    if isinstance(v, dict):
                        v = v.get('output_values', v)
                        # v = v.get(__name, v)

                    return v                

                r = f

            return r

        return super().__getattr__(__name)    
