import React from 'react'
import styled from 'styled-components'
import NewCountryForm from './NewCountryForm'

class Home extends React.Component {
  state = {
    isCreating: false
  }

  componentDidMount() {
    this.props.getData()
  }

  toggleCreate = (e) => {
    e.preventDefault()
    this.setState({ isCreating: !this.state.isCreating })
  }

  render() {
    return (
      <>
        {
          this.state.isCreating ? (
            <Div1>
              <NewCountryForm
                toggleCreate={this.toggleCreate}
                addCountry={this.props.addCountry}
              />
              <Button1 onClick={e => this.toggleCreate(e)}>Cancel</Button1>
            </Div1>
          ) : (
              <Div1>
                <Div2>
                  {
                    this.props.countries.map(country => (
                      <Div3 key={country.country}>
                        <p><Span1>Country</Span1>: {country.country}</p>
                        <p><Span1>Capital</Span1>: {country.capital}</p>
                        <p><Span1>Wikipedia</Span1>: {country.wiki}</p>
                        {country.visited ? <p><Span1>Visited</Span1>: Yes</p> : <p><Span1>Visited</Span1>: No</p>}
                      </Div3>
                    ))
                  }
                </Div2>
                <Button1 onClick={e => this.toggleCreate(e)}>Add New</Button1>
              </Div1>
            )
        }
      </>
    )
  }
}

const Div1 = styled.div`
  text-align: center;
`
const Div2 = styled.div`
  display: flex;
  justify-content: space-evenly;
`
const Div3 = styled.div`
  border: 1px solid #61dafb;
  border-radius: 5px;
  margin: 1rem;
  padding: 1rem;
`
const Span1 = styled.span`
  font-weight: 700;
`
const Button1 = styled.button`
  width: 100px;
  margin: 1rem auto;
  background: #61DAFB;
  padding: 5px;
  font-size: 16px;
  border-radius: 2px;
  border: none;
  box-shadow: 0 2px 2px gray;
  &:hover {
    cursor: pointer;
  }
`

export default Home