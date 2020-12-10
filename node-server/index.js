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
        let status = body.payload.object.presence_status
        console.log(status)
        if(status === 'Do_Not_Disturb') {

        } else if (status === 'Available') {

        } else {
            
        }
        res.setHeader('Content-Type', 'application/json')
        res.end(JSON.stringify(body))
    })
})

router.get('/', (req, res) => {
    res.end('Welcome to the door sign!')
})

const server = http.createServer((req, res) => {
    router(req, res, (req, res) => {})
})

server.listen(8080)