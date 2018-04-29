var parser = require('../');
var fs = require('fs');
var Json2csvParser = require('json2csv').Parser;
var FileSaver = require('file-saver');
var parse = require('csv-parse')
var sleep = require('sleep');

readCSV();
function readCSV(){

    fs.readFile('../../../../data/imdb_unique_prod-2018-04-21_0924.csv', function (err, fileData) {
      parse(fileData, {columns: true}, function(err, rows) {
        // Your CSV data is in an array of arrys passed to this callback as rows.
        //console.log(rows);
        readSRT(rows)
      })
    })
}
function readSRT(films) {
    var filepath = '../../../../data/srt/srt'
    fs.readdir(filepath, function(err, items) {
        var counter = 0;
        for (var i=0; i<items.length; i++) {
            var movie_srt = items[i].slice(0, -4);
            for (var j = 0; j < films.length; j++){
                var movie_csv = films[j]['title'];
                movie_csv = movie_csv.replace(/:/g,'-') + " " + parseInt(films[j]['year'])
                movie_csv = movie_csv.replace(/ /g,'-')
                
                if (movie_csv.toString().trim()  == movie_srt.toString().trim()){
                    counter++;
                    console.log(counter, movie_srt, movie_csv);
                    parseSRT(movie_csv,films[j])
                }
            }
        }
        
        
    });
}

//console.log(items);
        
        // match csv data here, pass into parseSRT along with movie
        

function parseSRT(fn,film){
    console.log("here")
    var filename = fn + '.srt';
    var srt = fs.readFileSync('../../../../data/srt/srt/'+filename, { encoding: 'utf-8' });
    var total_data = parser.fromSrt(srt,true);
    console.log("here")
    
    // clean rows
    for (i = 0; i < total_data.length; i++){
        var data = total_data[i]
        if(data['text']){
            data['text'] = data['text'].replace(/<(?:.|\n)*?>/gm, ''); // remove tags from text
            data['text'] = data['text'].replace('\n', ''); // remove tags from text
        }
        data['title'] = film['title'];
    }

    var fields = ["id","startTime","endTime","text","title"];

    var json2csvParser = new Json2csvParser({ fields });
    var csv = json2csvParser.parse(total_data);
    filename = filename.slice(0, -4)
    
    fs.writeFile('../../../../data/srt/srt_csv/'+filename+'.csv', csv, function(err) {
        console.log("5")
        if(err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    }); 
}