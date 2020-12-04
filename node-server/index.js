const http = require('http')
const Router = require('router')

const router = Router()

router.post('/', (req, res) => {
    res.setHeader('Content-Type', 'application/json')
    console.log(req)
    res.end(JSON.stringify(req))
})

const server = http.createServer((req, res) => {
    router(req, res, (req, res) => {})
})

server.listen(8080)