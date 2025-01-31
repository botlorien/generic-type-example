from typing import TypeVar, Generic


class Refuse:
    """Any refuse."""


class Biodegradable(Refuse):
    """Biodegradable refuse."""


class Compostable(Biodegradable):
    """Compostable refuse."""


T_contra = TypeVar('T_contra', contravariant=True)


class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        """Store trash until dumped."""


def deploy(trash_can: TrashCan[Biodegradable]):
    """Deploy a trash can for biodegradable refuse"""


if __name__ == '__main__':
    bio_can: TrashCan[Biodegradable] = TrashCan()
    deploy(bio_can)

    trash_can: TrashCan[Refuse] = TrashCan()
    deploy(trash_can)

    comp_can: TrashCan[Compostable] = TrashCan()
    deploy(comp_can)
