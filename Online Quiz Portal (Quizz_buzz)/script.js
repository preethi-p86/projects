const quiz_box = document.querySelector(".quiz_box");
const option_list = document.querySelector(".option_list");
const TimeCount = quiz_box.querySelector(".timer .time_sec");
const next_btn = quiz_box.querySelector(".next_btn");
const result_box = document.querySelector(".result_box");
const restart_quiz = result_box.querySelector(".buttons .restart");
const quit_quiz = result_box.querySelector(".buttons .quit");


let counter;
let que_count = 0;
let que_numb=1;
let time_value = 15;
let userScore = 0;
let tick = '<div class="icon tick"><i class="fas fa-check"></i></div>';
let cross = '<div class="icon cross"><i class="fas fa-times"></i></div>';

showQuestions(0);
queCounter(1);
StartTimer(15);
next_btn.style.display = "none";

restart_quiz.onclick =()=>{
	window.location.reload();
}

quit_quiz.onclick =()=>{
	location.href = "Activity.html";
}

next_btn.onclick = () =>
{
	if(que_count < questions.length - 1){
		que_count++;
		que_numb++;
		showQuestions(que_count);
		queCounter(que_numb);
		clearInterval(counter);
		StartTimer(time_value);
	}
	else{
		console.log("Questions Completed");
		console.log(userScore);
		showResultBox();
	}
	
}

function showQuestions(index){
	const que_text = document.querySelector(".que_text");
	let que_tag = '<span>' + questions[index].numb +"." +questions[index].question + '</span>';
	let option_tag = '<div class="option">'+questions[index].options[0]+'<span></span></div>'
					+ '<div class="option">'+questions[index].options[1]+'<span></span></div>'
					+ '<div class="option">'+questions[index].options[2]+'<span></span></div>'
					+ '<div class="option">'+questions[index].options[3]+'<span></span></div>';
	que_text.innerHTML = que_tag;
	option_list.innerHTML = option_tag;
	const option = option_list.querySelectorAll(".option");
	for(let i=0;i<option.length;i++){
		option[i].setAttribute("onclick","optionSelected(this)");
	}
}


function optionSelected(answer){
	clearInterval(counter);
	let userAns = answer.textContent;
	let correctAns = questions[que_count].answer;
	let allOptions = option_list.children.length;
	if(userAns == correctAns){
		userScore+=10;
		console.log(userScore);
		answer.classList.add("correct");
		console.log("CORRECT ANSWER");
		answer.insertAdjacentHTML("beforeend",tick);
	}else{
		userScore-=10;
		console.log(userScore);
		answer.classList.add("incorrect");
		console.log("WRONG ANSWER");
		answer.insertAdjacentHTML("beforeend",cross);
	}

	//once user selected disabled all options
	for(let i = 0;i < allOptions;i++){
		option_list.children[i].classList.add("disabled");
	}
	next_btn.style.display = "block";
}

function StartTimer(time){
	counter = setInterval(timer,1000);
	function timer(){
		TimeCount.textContent =time;
		time--;
		if(time < 9){
			let zero_add = TimeCount.textContent;
			TimeCount.textContent = "0" + zero_add;
		}
		if(time <= 0){
			clearInterval(counter);
			TimeCount.textContent = "00";

			let correctAns = questions[que_count].answer;
			let allOptions = option_list.children.length;
			
			for(let i=0; i<allOptions; i++){
				if(option_list.children[i].textContent==correctAns){
					option_list.children[i].setAttribute("class","option correct");
					option_list.children[i].insertAdjacentHTML("beforeend",tick);
				}

			}
			for(let i = 0;i < allOptions;i++){
		option_list.children[i].classList.add("disabled");
	}
	next_btn.style.display = "block";
		}
	}
}

function showResultBox(){
	quiz_box.classList.remove("activeQuiz");
	result_box.classList.add("activeResult");
	const scoreText = result_box.querySelector(".score_text");
	if(userScore > 30){
		let scoreTag = '<span><p>Congrats !! You got</p><p>' + userScore + '</p><p>out of</p><p>' + ((questions.length)*10) + '</p></span>';
		scoreText.innerHTML = scoreTag;
	}
	else{
		let scoreTag = '<span><p>Oh, No !! You got only </p><p>' + userScore + '</p><p>out of</p><p>' + ((questions.length)*10) + '</p></span>';
		scoreText.innerHTML = scoreTag;
	}
}

function queCounter(index){
	const bottom_ques_count = quiz_box.querySelector(".total_que");
	let totalQuesCountTag = '<span><p>' + index +'</p><p>of</p><p>'+ questions.length +'</p><p>Questions</p></span>';
	bottom_ques_count.innerHTML = totalQuesCountTag;
}


