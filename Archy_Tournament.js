// let n = require("readline-sync");
// let user = n.question("enter a number: ");

const players = require('./Archy_Tournament.json');
// console.log(typeof(players));

const ShowParticipants = (players) => {
    console.log(players)
    // console.log(players.team1)
    // players.map(player => (
    //     console.log(player)
    // ))
    // for(var i=0; i < players.length; i++) {
    //     console.log(i)
    // }
}

console.log(ShowParticipants(players))