import React from 'react'

const Home = (props) => {
  return (
    <div>
      <button onClick={e => props.logout(e)}> Logout</button>
    </div>
  )
}

export default Home