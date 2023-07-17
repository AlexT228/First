let r = "+";
let res = 0;

function sign_of(sign){
    r = sign;
    return r
}

function rez(){
    const ch1 = Number(document.getElementById("num1").value)
    const ch2 = Number(document.getElementById("num2").value)
    const answer_text = document.getElementById("answer");
    if (r == "+"){
        res = ch1 + ch2;
    }
    else if (r == "-"){
        res = ch1 - ch2;
    }else if (r == "*"){
        res = ch1 * ch2;
    }else{
        res = (ch1 / ch2).toFixed(2);
    }
    
    answer_text.style.fontSize = '100px';
    answer_text.style.rotate = "10deg";
    answer_text.innerHTML = String(res)
    setTimeout(function(){answer_text.style.fontSize = '25px';}, 1000)
    
}
