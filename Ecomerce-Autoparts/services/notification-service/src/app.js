const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Hello from Node.js Microservice!");
});

app.listen(3000, () => {
    console.log("Node.js microservice running on port 3000");
});
