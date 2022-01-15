import React from 'react'

const Hello = (props) => {

  return (
    <div>
      <h1>Hello World {props.name}, you age {props.age}</h1>
    </div>
  )
}
const App = () => {
  
  return (
  <div>
    <h1>Hello World</h1>
    <p>This is really working!</p>
  
    <p>Hello world</p>
    <Hello name = "Sara" age={34 + 43}/>
 
  </div>
)
  }

export default App

