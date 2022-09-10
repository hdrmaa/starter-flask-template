if __name__ == "__main__":
    import sys
    path = "/var/www/webroot/ROOT"
    if path not in sys.path:
        sys.path.append(path)

    from starterPack import create_app
    app = create_app()
    app.run()
