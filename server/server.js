const express = require('express');
const axios = require('axios');

const axiosInstance = axios.create({timeout: 5000});

const app = express();
const port = 80;

app.get('/', async (req, res) => {
    const ip = await loadPublicIp();
    
    res.send(getResponseHtml(ip));
})

app.get('/ip', async (req, res) => {
    const ip = await loadPublicIp();
    
    res.send(ip);
})

app.listen(port, () => console.log(`Server listening on port ${port}`))

function getResponseHtml(ip) {
    if (ip) {
        return `<!DOCTYPE html> <html> <body><center><h1>Ip address</h1></center>
        <center><p style=\"font-size:100%\">last updated: &lt ${new Date()} &gt publicIp: &lt<font color=\"blue\">${ip}</font>&gt</p></center>
        </body> </html>`;
    }
    return `<!DOCTYPE html> <html> <body><center><h1>Ip address</h1></center>
    <center><p style=\"font-size:100%\">failed to load ip from https://api.ipify.org/</p></center> 
    </body> </html>`;
}

async function loadPublicIp() {
  try {    
    const response = await axiosInstance.get('https://api.ipify.org/');
    return response.data;
  } catch (error) {
    console.log(`error while requesting ip: ${error.message}` )
  }
}