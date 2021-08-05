function buttonPress(){
    var url = $('#testSite').val();
    
    checkSite(url);
}



function checkSite(site){
    
    $.get('test_it/', {testSite:site})
        .done(function(data){
            const obj = JSON.parse(data);
            if (obj.site == 200){
                alert('Site is reachable!');
            }
            else{
                alert('Site not there!');
            }
            
        });
    
}