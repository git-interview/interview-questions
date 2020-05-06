
document.addEventListener("DOMContentLoaded", function(){

  const toggleAnswerIcon = [
    '▽',
    '△',
  ]

  const showAnswer = function(question) {
    var icon = question.querySelector('.toggle-answer-icon')
    icon.textContent = toggleAnswerIcon[1]
    var answer = question.parentElement.querySelector('.answer')
    answer.style.display = 'block'
  }

  const hideAnswer = function(question) {
    var icon = question.querySelector('.toggle-answer-icon')
    icon.textContent = toggleAnswerIcon[0]
    var answer = question.parentElement.querySelector('.answer')
    answer.style.display = 'none'
  }

  const toggleAnswer = function(question) {
    var icon = question.querySelector('.toggle-answer-icon')
    if (icon.textContent === toggleAnswerIcon[0]) {
      showAnswer(question)
    } else {
      hideAnswer(question)
    }
  }


  // the user can simultaneously toggle the visilibility of all answers
  const toggleAllAnswersText = [
    'Show all answers ▽',
    'Hide all answers △',
  ]

  var toggleAllAnswers = document.querySelector('.toggle-all-answers-button')
  jtd.addEvent(toggleAllAnswers, 'click', function(){
    if (toggleAllAnswers.textContent === toggleAllAnswersText[0]) {
      // show all answers
      toggleAllAnswers.textContent = toggleAllAnswersText[1]
      document.querySelectorAll('.question').forEach(function(question){
        showAnswer(question)
      })
    } else {
      // hide all answers
      toggleAllAnswers.textContent = toggleAllAnswersText[0]
      document.querySelectorAll('.question').forEach(function(question){
        hideAnswer(question)
      })
    }
  })


  // the user can individually toggle the visibility of each answer
  document.querySelectorAll('.question').forEach(function(question){
    jtd.addEvent(question, 'click', function(){
      toggleAnswer(question)
    })
  })

})
