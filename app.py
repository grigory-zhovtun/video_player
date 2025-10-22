from livereload import Server


def rebuild():
    ... # do things
    print("Site rebuilt")

rebuild()

server = Server()

server.watch('index.html', rebuild)
server.watch('css/*.css', rebuild)

server.serve(root='.', default_filename='index.html')

