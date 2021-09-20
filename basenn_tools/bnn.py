import base64
from mimetypes import guess_extension, guess_type
from typer import BadParameter
from io import BytesIO
import uuid
import os

base_dir = os.path.abspath('')


class Decode:
    def __init__(self, bnn: str, enc_string: str, mt: str, dl: str) -> None:
        try:
            mt, enc_string = enc_string.split(',')
            mt = mt.split(':')[1].split(';')[0]
            enc_string = enc_string
        except ValueError:
            print("[Info] Didn't found mimetype from encoding. If you are interested enter using --mt argument")
        finally:
            self.mimetye = mt
            self.bnn = bnn
            self.enc_string = enc_string
            if mt is not None:
                self.ext = self._guess_extension()

            # self.decode()


    def _guess_type(self) -> str:
        return guess_type(self.mimetye[0])
    
    def _guess_extension(self) -> str:
        return guess_extension(self.mimetye)
    
    def _bnn_decode(self):
        return {
            "b64": base64.b64decode,
            "b16": base64.b16decode,
            "b32": base64.b32decode,
            "b85": base64.b85decode
        }
    
    def decode(self):
        try:
            decoded_str = self._bnn_decode()[self.bnn](self.enc_string)
        except KeyError:
            raise BadParameter(
                f"{self.bnn} is not a valid parameter for --b argument. Did you mean "
                f"{' or '.join(i for i in self._bnn_decode().keys())}?"
            )
        return decoded_str.decode('utf-8')
    
    def decode_and_save(self):
        file_name = f"{uuid.uuid4()}{self.ext}"
        file_name = os.path.join(base_dir, file_name)
        decoded_str = self._bnn_decode()[self.bnn](self.enc_string)
        with open(file_name, 'wb') as file:
            file.write(decoded_str)
        return f"File saved file on {file_name}"
