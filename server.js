var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000,
  SalesBell = require('./api/models/salesBellModel'),
  bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


var routes = require('./api/routes/salesBellRoutes'); //importing route
routes(app); //register the route

app.listen(port);

console.log('Sales Bell RESTful API server started on: ' + port);