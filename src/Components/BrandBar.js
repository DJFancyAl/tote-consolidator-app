import { useTheme } from '@material-ui/core';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import useScrollTrigger from '@mui/material/useScrollTrigger';
import Slide from '@mui/material/Slide';
import WarehouseIcon from '@mui/icons-material/Warehouse';

function HideOnScroll({children}) {
    const trigger = useScrollTrigger();
  
    return (
      <Slide appear={false} direction="down" in={!trigger}>
        {children}
      </Slide>
    );
  }

const BrandBar = () => {
  const theme = useTheme();

  return (
      <>
        <HideOnScroll>
          <AppBar sx={{backgroundColor: theme.palette.primary.dark, color: theme.palette.primary.main}}>
            <Toolbar sx={{justifyContent: 'center'}}>
              <WarehouseIcon sx={{ mr: 2 }} />
              <Typography
                variant="h5"
                noWrap
                component="a"
                href="/"
                sx={{
                  mr: 2,
                  fontFamily: 'roboto',
                  fontWeight: 700,
                  color: 'inherit',
                  textDecoration: 'none'
                }}
              >
              Tote Consolidator
              </Typography>
            </Toolbar>
          </AppBar>
        </HideOnScroll>
        <Toolbar />
    </>
  )
}

export default BrandBar