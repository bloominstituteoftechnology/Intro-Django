import React, { Component } from 'react'
import logo from './logo.svg'
import styled from 'styled-components'
import Login from './components/Login'
class App extends Component {
  render() {
    return (
      <Div1>
        <Img1 src={logo} alt="logo" />
        <Login />
      </Div1>
    )
  }
}

const Div1 = styled.div`
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`

const Img1 = styled.img`
  animation: App-logo-spin1 infinite 30s linear;
  height: 20vmin;

  @keyframes App-logo-spin1 {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}
`

export default App;
