import { useTheme } from '@material-ui/core';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import WidgetsIcon from '@mui/icons-material/Widgets';
import BorderAllIcon from '@mui/icons-material/BorderAll';
import RectangleIcon from '@mui/icons-material/Rectangle';

const Navbar = ( { location, setLocation } ) => {
    const theme = useTheme();
    
    const activeStyle = {
        color: theme.palette.primary.dark,
        backgroundColor: theme.palette.primary.main
    }
    
    const inactiveStyle = {
        color: theme.palette.secondary.main,
        backgroundColor: theme.palette.primary.dark
    }

    return (
        <BottomNavigation showLabels sx={{backgroundColor: theme.palette.primary.dark}}>
            <BottomNavigationAction
            sx={location === 'rave' ? activeStyle : inactiveStyle}
            label="Rave"
            icon={<WidgetsIcon />}
            onClick={() => setLocation('rave')}
            />
            <BottomNavigationAction
            sx={location === 'jaco' ? activeStyle : inactiveStyle}
            label="Jaco"
            icon={<BorderAllIcon />}
            onClick={() => setLocation('jaco')}
            />
            <BottomNavigationAction
            sx={location === 'all' ? activeStyle : inactiveStyle}
            label="All"
            icon={<RectangleIcon />}
            onClick={() => setLocation('all')}
            />
        </BottomNavigation>
    )
}

export default Navbar