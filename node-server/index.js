const http = require('http')
const Router = require('router')

const router = Router()

router.get('/', (req, res) => {
    res.setHeader('Content-Type', 'application/json')
    res.end(JSON.stringify({ hello: 'world'}))
})

const server = http.createServer((req, res) => {
    router(req, res, (req, res) => {})
})

server.listen(8080)