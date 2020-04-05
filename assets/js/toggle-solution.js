
document.addEventListener("DOMContentLoaded", function(){

  const toggleSolutionText = [
    'Show solution ▽',
    'Hide solution △',
  ]

  var toggleSolution = document.querySelector('.toggle-solution-button')
  var solution = document.querySelector('.solution')
  jtd.addEvent(toggleSolution, 'click', function(){
    if (toggleSolution.textContent === toggleSolutionText[0]) {
      // show solution
      toggleSolution.textContent = toggleSolutionText[1]
      solution.style.display = 'block'
    } else {
      // hide solution
      toggleSolution.textContent = toggleSolutionText[0]
      solution.style.display = 'none'
    }
  })

})
