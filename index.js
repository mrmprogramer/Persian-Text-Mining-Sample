
let onload=()=>{
}

let Search=()=>{
   
    $.ajax({
        url: "http://127.0.0.1:5000/Search",
        type: 'GET', 
        cors: true ,
        contentType:'application/json',
        secure: true,
        data: {
            query: document.getElementById('Search-input').value
        },
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
        
        success: function (data){
            obj=JSON.parse(data)
            IDf(obj);
            rank(obj);
        }
    })
}

let rank=(data)=>{
    
    for(var item in data.response){
        data.response[item].maxtfidf=0;
        data.response[item].tfmax=0;
        data.response[item].cosinos=0;
        for(var tindex in data.response[item].tfidf){
            data.response[item].maxtfidf+=data.response[item].tfidf[tindex].tfidf,
            data.response[item].tfmax+=data.response[item].tfidf[tindex].tf,
            data.response[item].cosinos*=data.response[item].tfidf[tindex].tfidf
        }
    }


    data.response.sort((firstItem, secondItem) => firstItem.tfmax > secondItem.tfmax);
    data.response.reverse();

    console.log(data)
    DrawResult(data);
}









let DrawResult=(data)=>{
var response = data.response;

var str = '';
for(var item in response){
    str += '<div class=" card " style="margin:3px;" dir="rtl"><div class="col-6"><a class="row"  href="./datamodel/'+response[item].filename+'" download="'+response[item].filename+'"><span class="col-4">'+response[item].filename+'</span></a> <span class="col-4" style="margin:3px;">تعداد تکرار :' +response[item].tfmax+'</span> <span class="col-4" style="margin:3px;">max tf-idf :' +response[item].maxtfidf+'</span></div></div>';
}

document.getElementById('resultbox').innerHTML = str;


}
let IDf=(data)=>{
    var response = data.response;
    var dflist = data.dfwordlist;
    for(var item in response){
        for(var word in response[item].words){
           var tf = parseInt(response[item].words[word].count);
           for(var wordf in dflist){
               if(dflist[wordf].word == response[item].words[word].word)
                var df = dflist[wordf].files.length;
           }
           response[item].tfidf = []
           response[item].tfidf.push({
               tf:tf,
               df:df,
               tfidf:Math.log(1+tf)*Math.log10(data.doccount/df)
           })
        }
    }
    
}
