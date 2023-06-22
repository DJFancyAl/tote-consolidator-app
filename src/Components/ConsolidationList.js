import { useEffect, useState } from 'react';
import axios from 'axios';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import Alert from '@mui/material/Alert';
import Consolidation from './Consolidation';
import PullToRefresh from 'react-simple-pull-to-refresh';
import RiseLoader from "react-spinners/RiseLoader";

const ConsolidationList = ({location}) => {
  const [consolidations, setConsolidations] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [alert, setAlert] = useState('')

  async function fetchData() {
    try {
      setIsLoading(true)
      const response = await axios.post('http://192.168.108.44:5000/', {"location": location, timeout: 8000}) // 8 Seconds
      const data = response.data
      if(data.error) {
        setAlert(data.error)
      } else {
        setConsolidations(data)
        setAlert('')
      }
      setIsLoading(false)
    } catch(e) {
      setIsLoading(false)
      setAlert(e.message)
    }
  }
  
  // Fetch Consolidations
  useEffect(() => {
    fetchData()
  }, [location])

  
  // Handles the pull-down refresh
  const handleRefresh = () => {
    return new Promise((resolve, reject) => {
      fetchData()
    })
  }
  
  // Create the item list
  const items = consolidations.map((item, index) => {
    return (
      <Consolidation key={index} consolidation={item} />
    )
  })

  // Alert
  const alertMessage = (
    <Container sx={{mt: 2, display: 'flex', justifyContent: 'center', alignItems: 'start', flexGrow: 1, minHeight: '300px'}}>
      <Alert severity="error">Oh no! There was an error: {alert}</Alert>
    </Container>
  )

  // Show Message if there's no consolidations
  const noConsolidations = (
      <Container sx={{mt: 2, display: 'flex', justifyContent: 'center', alignItems: 'start', flexGrow: 1, minHeight: '300px'}}>
        <Alert variant="standard" severity="info">No consolidations! Refresh to try again.</Alert>
      </Container>
  )

  // Show loading animation
  if(isLoading){
    return (
      <Container sx={{mt: 2, display: 'flex', justifyContent: 'center', alignItems: 'center', flexGrow: 1}}>
        <RiseLoader size={60} color='#37832b' />
      </Container>
    )
  }

  return (
    <Container maxWidth="md" sx={{my: 2, flexGrow: 1}}>
      <PullToRefresh onRefresh={handleRefresh} pullingContent='' resistance={3}>
        {alert && alertMessage}
        {!alert && consolidations.length === 0 && noConsolidations}
        <Stack spacing={2}>
          {items}
        </Stack>
      </PullToRefresh>
    </Container>
  )
}

export default ConsolidationList