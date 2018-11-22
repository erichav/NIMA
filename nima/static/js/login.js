var config = {
    apiKey: "AIzaSyCZ26gsPtgaK-AEWx50y2ipY0_L2pFASf0",
    authDomain: "nima-72515.firebaseapp.com",
    databaseURL: "https://nima-72515.firebaseio.com",
    projectId: "nima-72515",
    storageBucket: "nima-72515.appspot.com",
    messagingSenderId: "650787506289"
  };


//login
function setCookie(cname,cvalue,exdays) {
    let d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

const loginUser = async (uid, name, email) => {
	console.log("loginUser");
	const url = "https://localhost:3000/api/login";
	try{
		let respo = await axios.post('/api/login', {
			uid: uid,
			name: name,
			email: email
		});
	}catch (err){
		console.log(err);
	}
};


async function saveUser(user, token){
	let uid = user.uid;
	if(!uid||!token)
		return;

	setCookie("AT", token, 15);

	await loginUser(uid, user.displayName, user.email);

	location.reload(true);
}

async function loginFacebook(){
	firebase.auth().signInWithPopup(provider)
	.then(function(result){
		let token= result.credential.accessToken;
		let user= result.user;
		saveUser(user, token);
	}).catch(function(error){
		console.log(error.message);
	});
}
function logoutFacebook(){
	firebase.auth().signOut()
	.then(function(){
		console.log('Signed Out')
	},function(error){
		console.log('Failed');
	});
}

function loginGoogle(){
	firebase.initializeApp(config);
	var googleAuthProvider = new firebase.auth.GoogleAuthProvider
	firebase.auth().signInWithPopup(googleAuthProvider)
	.then(function(result){
		console.log("success")
		console.log(result)
		window.location.href = 'agregar_producto';
	}).catch(function(err){
		console.log(err)
	})
}
function logOutGoogle(){
	firebase.auth().signOut()
	.then(function(){
		console.log('Signed Out')
	},function(error){
		console.log('Failed');
	});
}

function sendMail() {
	var link = "mailto:adri130497@gmail.com"
	+ "&subject=" + escape("Login")
	+ "&body=" + escape(document.getElementById('myText').value);
	window.location.href = link;
}