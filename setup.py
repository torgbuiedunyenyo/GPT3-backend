from examples.run_jeremy_code import gpt, config, demo_web_app
app = demo_web_app(gpt, config)

if __name__ == '__main__':
    app.run()