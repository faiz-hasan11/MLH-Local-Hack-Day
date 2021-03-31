import './App.css';
import {Button, Paper, TextField} from "@material-ui/core"
import { useState , useEffect} from 'react';
import {auth} from "./firebase"
function App() {
  const [name,setName] = useState("")
  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")
  const [user,setUser] = useState(null)

   useEffect(() =>
    {
        const unsubscribe = auth.onAuthStateChanged((authUser) =>
        {
            if(authUser)
            {
                setUser(authUser)
            }
            else
            {
                setUser(null)
            }
        })
        return () =>
        {
            unsubscribe()
        }
    },[user,name])

  const handleSubmit = (e) =>
  {
        console.log(name,email,password)
        e.preventDefault()
        auth.createUserWithEmailAndPassword(email,password)
        .then((authUser) => {
            return authUser.user.updateProfile({
                displayName:name
            })
        })
        .catch((error) => alert(error.message))
        setName("")
        setPassword("")
  }


  return (
    <div className="root">
      <div className="header">
        Authentication System
      </div>      
        { user ?
          (<div className="data">
            {console.log(user.displayName)}
              <h1>Welcome {user.displayName}</h1>
              <Button variant="contained" color="primary" onClick={() => auth.signOut()}>Logout</Button>
          </div>)
        :
        (<Paper className="paper">
          <form className="form" noValidate autoComplete="off">
            <div className="input"><TextField id="standard-basic" label="name" value={name} onChange={(e) => setName(e.target.value)}/></div>
            <div className="input"><TextField id="standard-basic" label="email" value={email} onChange={(e) => setEmail(e.target.value)}/></div>
            <div className="input"><TextField id="standard-basic" label="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)}/></div>
            <div className="btn"><Button variant="contained" color="primary" onClick={handleSubmit}>Sign In</Button></div>
          </form>
        </Paper> ) }      
      
    </div>
  );
}

export default App;
