const express = require('express')
const app = express()
const port = 3000

app.get('/e', (req, res) => {
  res.json({
      message : 'hello world ! '
  })
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})



