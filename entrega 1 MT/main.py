"""Interfaz de consola (esqueleto de la Entrega 1)."""


def mostrar_menu() -> None:
    print("\n=== Juego tipo Metal Slug · esqueleto ===")
    print("1. Iniciar partida (pendiente)")
    print("0. Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        print("Funcionalidad aún no implementada.")


if __name__ == "__main__":
    main()
