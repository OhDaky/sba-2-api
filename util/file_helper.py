from dataclasses import dataclass

@dataclass
class FileReader:

    cotext: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''