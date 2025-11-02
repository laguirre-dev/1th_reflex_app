import reflex as rx
import pandas as pd
from ReflexApp1.components.form import form_field, form_title


class State(rx.State):
    # Lista de ingredientes
    ing_list: dict = {"Ingrediente": [], "Precio": []}

    # crea Dataframe con los ingredientes
    @rx.var
    def df(self) -> pd.DataFrame:
        return pd.DataFrame(self.ing_list)

    # Evento de agregacion de ingrediente al diccionario
    @rx.event
    def add_ing(self, form_data: dict):
        if not form_data["ingrediente"] or not form_data["ing_precio"]:
            return
        self.ing_list["Ingrediente"].append(form_data["ingrediente"])
        self.ing_list["Precio"].append(int(form_data["ing_precio"]))

    # Calculo del costo total
    @rx.var
    def costo_total(self) -> float:
        costo = self.df["Precio"].sum()
        return int(costo)


def index() -> rx.Component:
    return rx.container(
        rx.heading("¡Bienvenidos a mi primera aplicacion con Reflex!", color_scheme="tomato", align="center", font_size="3rem", weight="bold", margin="1em 0"),
        rx.flex(
            rx.card(
                rx.flex(
                    form_title(
                        icon="list-check",
                        title="Calculadora de costos totales de ingredientes",
                        subtitle="La aplicacion permite calcular el gasto total de ingredientes necesarios",
                    ),
                    rx.form.root(
                        rx.flex(
                            form_field("Ingrediente", "text", "ingrediente"),
                            form_field("Precio", "number", "ing_precio"),
                            direction="column",
                            spacing="2",
                        ),
                        rx.form.submit(
                            rx.button("Agregar", size="3"),
                            as_child=True,
                            width="100%",
                        ),
                        on_submit=State.add_ing,
                        reset_on_submit=True,
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Costo Total: ", size="4", weight="bold"),
                        rx.text(
                            f"${State.costo_total}",
                            font_size="3rem",
                            weight="bold",
                            color_scheme="grass",
                        ),
                        align="center",
                        spacing="2",
                        justify="center",
                    ),
                    width="100%",
                    direction="column",
                    spacing="4",
                ),
                width="100%",
                size="4",
            ),
            rx.card(
                rx.heading("Lista de Ingredientes", size="4", weight="bold"),
                rx.data_table(
                    data=State.df,
                    pagination=True,
                    search=True,
                    sort=True,
                ),
                width="100%",
                size="4",
                background_color="gray.100",
            ),
            width="100%",
            spacing="4",
        ),
        size="4"
    )


app = rx.App(
    theme=rx.theme(color_mode="light", accent_color="tomato", gray_color="mauve")
)
app.add_page(index)
