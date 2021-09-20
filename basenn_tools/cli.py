from v import version
from bnn import Decode
from typing import Optional, List
import typer


app = typer.Typer()

@app.command('version')
def version(version: str = version):
    msg = f"[Info] version {version}"
    msg = typer.style(msg, fg=typer.colors.BRIGHT_GREEN)
    typer.echo(msg, color=True)

@app.command('decode')
def decode(
        b: str = typer.Option(
            "b64", help=f"Enter Decoding type:\nbase16: b16\nbase32: b32,\nbase64:b64\nbase85: b85"
        ),
        d: str = typer.Option(
            None, help="Enter your encoded string for decode"
        ),
        mt: Optional[str] = typer.Option(
            None, help="Enter mimetype"
        ),
        dl: Optional[str] = typer.Option(
            None, help="Enter destination location to save file"
        )
    ):
    try:
        d = Decode(b, d, mt, dl)
        result = typer.style(d.decode_and_save(), fg=typer.colors.BRIGHT_GREEN)
        typer.echo(f"[Info ] Decoded successfully: {result}", color=True)
    except typer.BadParameter as e:
         err = typer.style(f"[Error ] {e}", fg=typer.colors.BRIGHT_RED)
         typer.echo(err, color=True)

if __name__ == "__main__":
    app()