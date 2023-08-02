var form =document.querySelector('#postForm')


form.addEventListener('submit', (e)=>{
	e.preventDefault()
//	document.getElementById('result').innerHTML = "Patientez..."
	document.getElementById('result').innerHTML = `
<div class="text-center">
  <div class="spinner-border" role="status">
    <span class="visually-hidden"></span>
  </div>
</div>`

	var nbre1 = document.getElementById('a').value
	var nbre2 = document.getElementById('b').value
	var nbre3 = document.getElementById('c').value

	var param = {
		nb1:nbre1,
		nb2:nbre2,
		nb3:nbre3
	}

	var xhr = new XMLHttpRequest()

	xhr.open('post', '../output', true)
	xhr.setRequestHeader('Content-Type', 'application/json')

	xhr.onload = function(){
		console.log('PINTO')
		document.querySelector("#result").innerHTML=this.responseText
	}

	xhr.send(JSON.stringify(param))
})

var btn = document.getElementById('res')

btn.addEventListener('click',()=>{
	document.querySelector("#result").classList.add('active')
})