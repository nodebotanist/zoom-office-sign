const http = require('http')
const Router = require('router')

const router = Router()

router.post('/', (req, res) => {
    let body = ""
    req.on('data', (chonk) => {
        body += chonk
    })
    req.on('end', () => {
        body = JSON.parse(body)
        console.log(body)
        res.setHeader('Content-Type', 'application/json')
        res.end(JSON.stringify(body))
    })
})

const server = http.createServer((req, res) => {
    router(req, res, (req, res) => {})
})

server.listen(8080)