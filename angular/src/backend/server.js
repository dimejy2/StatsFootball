 var express = require('express');
 var app = express();
 var path = require('path');
 var dbSession = require('./dbSession.js');
 var cors = require('cors');
 // set the public folder to serve public assets
app.use(express.static(__dirname + '../frontend'));
app.use(cors());


app.get('/all', function(req, res) {
    dbSession.fetchAll('select * from my_app_player order by stat8 desc', 
            function(err, rows){
        if (err) {
            console.log(err);
            res.send(err); } 
        else {
            console.log(rows);
            res.send(rows);
        }
    }); 

});

app.get('/wr', function(req, res) {
    dbSession.fetchAll('select * from my_app_player WHERE pos = "WR" order by stat8 desc', 
            function(err, rows){
        if (err) {
            console.log(err);
            res.send(err); } 
        else {
            res.send(rows);
        }
    }); 

});

app.get('/qb', function(req, res) {
    dbSession.fetchAll('select * from my_app_player where pos="QB" order by stat8 desc', 
            function(err, rows){
        if (err) {
            console.log(err);
            res.send(err); } 
        else {
            res.send(rows);
        }
    }); 

});
app.get('/rb', function(req, res) {
    dbSession.fetchAll('select * from my_app_player where pos = "RB" order by stat8 desc', 
            function(err, rows){
        if (err) {
            console.log(err);
            res.send(err); } 
        else {
            res.send(rows);
        }
    }); 

});
app.get('/k', function(req, res) {
    dbSession.fetchAll('select * from my_app_player where pos = "K" order by stat8 desc', 
            function(err, rows){
        if (err) {
            console.log(err);
            res.send(err); } 
        else {
            res.send(rows);
        }
    }); 

});

app.get('/te', function(req, res) {
    dbSession.fetchAll('select * from my_app_player where pos = "TE" order by stat8 desc', 
            function(err, rows){
        if (err) {
            console.log(err);
            res.send(err); } 
        else {
            res.send(rows);
        }
    }); 

});
  
 app.get('*', function(req, res) {
 res.sendFile(path.join(__dirname + '/../frontend/index.html'));
 });

 // start the server on port 8080 (http://localhost:8080)
 app.listen(8000);
 console.log('Magic happens on port 8000.');

