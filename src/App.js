import { useState, useEffect } from 'react';
import { createTheme } from '@mui/material/styles';
import { ThemeProvider } from '@material-ui/core/styles';
import Paper from '@mui/material/Paper';
import BrandBar from './Components/BrandBar';
import ConsolidationList from './Components/ConsolidationList';
import Navbar from './Components/Navbar';

// Collect Location from localstorage
let storedLocation = localStorage.getItem("location");
if(storedLocation == null) storedLocation = 'rave';

const theme = createTheme({
  palette: {
    primary: {
      main: '#37832b',
      dark: '#212529',
      light: '#aaaaaa'
    },
    secondary: {
      main: '#FFEFE1',
    }
  }
});


function App() {
  // State
  const [location, setLocation] = useState(storedLocation)

  // Update Local Storage
  useEffect(() => {
    localStorage.setItem("location", location)
  }, [location])

  return (
    <ThemeProvider theme={theme}>
      <Paper sx={{maxWidth: '100vw', minHeight: '100vh', margin: '0', backgroundColor: theme.palette.primary.light, display: 'flex', flexDirection: 'column'}}>
        <BrandBar />
        <ConsolidationList location={location} />
        <Navbar location={location} setLocation={setLocation} />
      </Paper>
    </ThemeProvider>
  );
}

export default App;
