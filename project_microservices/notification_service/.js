const express = require('express');
const { Server } = require('socket.io');
const http = require('http');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

io.on('connection', (socket) => {
  console.log('Client connected');
  socket.on('notify', (message) => {
    io.emit('notification', message);
  });
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
