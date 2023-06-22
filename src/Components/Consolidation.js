import { useState } from 'react';
import { useTheme } from '@material-ui/core';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

const Consolidation = ({consolidation}) => {
    // State
    const theme = useTheme();
    const [checked, setChecked] = useState(false)

    // Style
    const style = {
        p: 1,
        backgroundColor: checked ? theme.palette.primary.main : theme.palette.primary.dark,
        color:  checked ? theme.palette.primary.dark : theme.palette.secondary.main,
        cursor: 'pointer'
    }

    const list = consolidation.map((item, index) => {
        return (
            <Grid key={index} container spacing={2} p={1}>
                <Grid item xs={3}>
                    <Typography variant="body2">{item.color} {item.size}</Typography>
                </Grid>
                <Grid item xs={3}>
                    <Typography variant="body2">{item.location}</Typography>
                </Grid>
                <Grid item xs={3}>
                    <Typography variant="body2">{item.batch}</Typography>
                </Grid>
                <Grid item xs={3}>
                    <Typography variant="body2">{item.weight} lbs.</Typography>
                </Grid>
            </Grid>
        )
    })

    return (
        <Paper elevation={4} sx={style} onClick={() => setChecked(!checked)}>
            <Stack divider={<Divider sx={{borderColor: checked ? theme.palette.primary.dark : theme.palette.secondary.main}} flexItem />}>
                {list}
            </Stack>
        </Paper>
    )
}

export default Consolidation