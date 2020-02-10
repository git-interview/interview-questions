
console.log('toggle answer loaded');


document.addEventListener("DOMContentLoaded", function(){


  const toggleAnswer = function(question) {
    var answer = question.querySelector('.answer')
    if (answer.style.display === 'block') {
      answer.style.display = 'none'
    } else {
      answer.style.display = 'block'
    }
  }


  document.querySelectorAll('.question').forEach(function(question){
    jtd.addEvent(question, 'click', function(){
      console.log('clicked question')
      toggleAnswer(question)
    })
  })


  const toggleAllAnswersText = [
    'Show all answers ▷',
    'Hide all answers ◁',
  ]

  var toggleAllAnswers = document.querySelector('.toggle-all-answers')
  jtd.addEvent(toggleAllAnswers, 'click', function(){
    console.log('clicked toggle all answers')
    toggleAllAnswers.textContent === toggleAllAnswersText[0] ?
      toggleAllAnswers.textContent = toggleAllAnswersText[1] :
      toggleAllAnswers.textContent = toggleAllAnswersText[0]

    document.querySelectorAll('.question').forEach(function(question){
      toggleAnswer(question)
    })
  })

})
