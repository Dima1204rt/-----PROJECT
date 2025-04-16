var correctAns = 0 //счетчик правильных ответов
var curExCount = 0 //счетчик количества оставшихся примеров
var maxExCount = 0 //переменная, хранящая количество примеров, которое выбрал юзер

function sendPOST(url, json, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) { //статус 200 означает, что запрос был успешным
        callback(null, JSON.parse(xhr.response));
      } else {
        callback(status, JSON.parse(xhr.response));
      }
    };
    xhr.send(JSON.stringify(json));
};

function generate(){
    let genNum=document.getElementById('genNum') //поиск элемента на странице с id 'genNum' и затем сохранение в переменную genNum для взаимодействия со значением
    let sys=document.getElementById('firstSelect')
    let direction=document.getElementById('secondSelect')
    sendPOST(
        '/api/generate', {
            'sys': sys.value, 
            'direction': direction.value,
        }, function(status, response) {
            if (status === null) {
                genNum.innerText=response.result //в элемент с id genNum вставляем значение result(сгенеренное число) текстом(.innerText), получаемое с сервера с помощью response
            }

        }
    )
    
let stats=document.getElementById('stats')
stats.style.display='none'

}
function onStartBtnPressed(){ //функция, описываающая что происходит при нажатии на кнопку СТАРТ
    let sumEx=document.getElementById('sumEx')
    let content=document.getElementById('content')
    let settings=document.getElementById('settings')
    let ostExCount=document.getElementById('ostExCount')
    let sys=document.getElementById('firstSelect')  //поиск элемента на странице с id 'firstSelect' и затем сохранение в переменную sys для взаимодействия со значением
    let direction=document.getElementById('secondSelect')
    let dircon=document.getElementById('dircon')
    let sysgencon=document.getElementById('sysgencon')
    let res=document.getElementById('result')
    document.getElementById("but").disabled = false; // кнопка активна
    if (direction.value === 'ИЗ десятичной'){
        if (sys.value === 'Двоичная'){
            dircon.innerText=`Направление перевода: в Двоичную`
            sysgencon.innerText=`(десятичная система счисления)`
        }
        if (sys.value === 'Восьмеричная'){
            dircon.innerText=`Направление перевода: в Восьмеричную`
            sysgencon.innerText=`(десятичная система счисления)`
        }
        if (sys.value === 'Шестнадцатеричная'){
            dircon.innerText=`Направление перевода: в Шестнадцатеричную`
            sysgencon.innerText=`(десятичная система счисления)`
        }

    }
    if (direction.value === 'В десятичную'){
        if (sys.value === 'Двоичная'){
            dircon.innerText=`Направление перевода: ${direction.value}`
            sysgencon.innerText=`(двоичная система счисления)`
        }
        if (sys.value === 'Восьмеричная'){
            dircon.innerText=`Направление перевода: ${direction.value}`
            sysgencon.innerText=`(восьмеричная система счисления)`
        }
        if (sys.value === 'Шестнадцатеричная'){
            dircon.innerText=`Направление перевода: ${direction.value}`
            sysgencon.innerText=`(шестнадцатеричная система счисления)`
        }
    }
    
    content.style.display='block' //проявление контейнера content
    settings.style.display='none' //исчезновение контейнера settings
    res.style.display='none'
    curExCount=Number(sumEx.value) //переменной curExCount присваиваем значение в виде числа, взятое из элемента с id sumEx
    maxExCount=curExCount //количество примеров, которое выбрал юзер равно кличеству оставшихся примеров при решении первого примера
    ostExCount.innerText=curExCount //в элемент с id ostExCount вставляем значение curExCount текстом(.innerText)
    generate() // запускаем функцию generate 

}

function onCheckBtnPressed(){ //функция, описывающая что происходит при нажатии на кнопку ПРОВЕРКА (замена циклу)
    let sys=document.getElementById('firstSelect')  //поиск элемента на странице с id 'firstSelect' и затем сохранение в переменную sys для взаимодействия со значением
    let direction=document.getElementById('secondSelect')
    let user_ans=document.getElementById('thirdField')
    let result=document.getElementById('result')
    let ostExCount=document.getElementById('ostExCount')
    let stats=document.getElementById('stats')
    

    sendPOST(
        '/api/check', { //запихиваем значения с сайта на сервер в функцию check(), которая в app.py
            'sys': sys.value, 
            'direction': direction.value,
            'user_ans': user_ans.value
        }, function(status, response) {
            if (status === null) {
                stats.style.display='none'
                result.style.display='block'
                result.innerText=response.result //в элемент с id result(смотри index.html) вставляем значение result(ПРАВИЛЬНО/НЕРПАВИЛЬНО) текстом(.innerText), получаемое с сервера с помощью response
                if (response.result === '✅ПРАВИЛЬНО✅') {
                    correctAns=correctAns + 1
                }  
                user_ans.value="" //очищаем поле для ввода числа
                curExCount-- //уменьшаем количество оставшихся примеров на 1
                ostExCount.innerText=curExCount //в элемент с id ostExCount вставляем значение curExCount текстом(.innerText)
                if (curExCount > 0) {
                    generate()
                }
                else{
                    document.getElementById("but").disabled = true; // кнопка теперь неактивна
                    window.setTimeout(function(){
                        content.style.display='none'
                        stats.style.display='block'
                        corans.innerText=correctAns
                        ngenEx.innerText=Number(sumEx.value)
                    }, 1100)

                }
                
            }                                                  

        }
    )
}

function onBackBtnPressed(){
    let stats=document.getElementById('stats')
    let settings=document.getElementById('settings')
    stats.style.display='none'
    settings.style.display='block'


}

    