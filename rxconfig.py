import reflex as rx

config = rx.Config(
    app_name="ReflexApp1",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)