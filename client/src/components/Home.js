import React from 'react'
import styled from 'styled-components'

class Home extends React.Component {
  componentDidMount() {
    this.props.getData()
  }

  render() {
    return (
      <Div>
        {
          this.props.countries.map(country => (
            <Div2 key={country.country}>
              <p><Span1>Country</Span1>: {country.country}</p>
              <p><Span1>Capital</Span1>: {country.capital}</p>
              <p><Span1>Wikipedia</Span1>: {country.wiki}</p>
              {country.visited ? <p><Span1>Visited</Span1>: Yes</p> : <p><Span1>Visited</Span1>: No</p>}
            </Div2>
          ))
        }
      </Div>
    )
  }
}

const Div = styled.div`
  display: flex;
  justify-content: space-evenly;
`
const Div2 = styled.div`
  border: 1px solid #61dafb;
  border-radius: 5px;
  margin: 1rem;
  padding: 1rem;
`
const Span1 = styled.span`
  font-weight: 700;
`

export default Home