import React, {useEffect, useState} from 'react';
import {
    Box,
    Grid,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography
} from "@mui/material";
import {LineChart, CartesianGrid, Legend, Line, ResponsiveContainer, Tooltip, XAxis, YAxis} from "recharts";

const Body = () => {
    const [data, setData] = useState();
    const [total, setTotal] = useState();
    const [valuesPerDay, setValuesPerDay] = useState();
    const getData = async () => {
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch('/api/data/', requestOptions);
        const answer = await response.json();

        if (response.ok) {
            setData(answer);
        }
    }

    const getTotal = async () => {
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch('/api/total/', requestOptions);
        const answer = await response.json();

        if (response.ok) {
            setTotal(answer);
        }
    }

    const getValuesPerDay = async () => {
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch('/api/per_day/', requestOptions);
        const answer = await response.json();

        if (response.ok) {
            setValuesPerDay(answer);
        }
    }

    useEffect(() => {
        getData();
        getTotal();
        getValuesPerDay();
    }, [])

    console.log(valuesPerDay);
    return (
        <Box sx={{mt: 8}}>
            <Grid item md={10} xs={12} sm={12} lg={8} xl={8}>
                <Paper elevation={0} sx={{display: "flex", justifyContent: 'center', alignItems: 'center'}}>
                    <Paper elevation={0}>
                        <Typography variant="h3">Total: {total}</Typography>
                    </Paper>
                    <Paper elevation={0}>
                        <LineChart width={812} height={300} data={valuesPerDay} margin={{top: 20}}>
                            <CartesianGrid strokeDasharray="3 3"/>
                            <XAxis dataKey="name"/>
                            <YAxis/>
                            <Tooltip/>
                            <Legend/>
                            <Line type="monotone" dataKey="value" stroke="#82ca9d"/>
                        </LineChart>
                    </Paper>
                </Paper>
                <Paper sx={{display: "flex", justifyContent: "center"}}>
                        <Table sx={{minWidth: 650, maxWidth: 1200}} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>№</TableCell>
                                    <TableCell align="right">заказ №</TableCell>
                                    <TableCell align="right">стоимость,$</TableCell>
                                    <TableCell align="right">стоимость,P</TableCell>
                                    <TableCell align="right">срок поставки</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {data?.map((row) => (
                                    <TableRow
                                        key={row.data_id}
                                        sx={{'&:last-child td, &:last-child th': {border: 0}}}
                                    >
                                        <TableCell component="th" scope="row">
                                            {row.data_id}
                                        </TableCell>
                                        <TableCell align="right">{row.order_num}</TableCell>
                                        <TableCell align="right">{row.price_dollar}</TableCell>
                                        <TableCell align="right">{row.price_rub}</TableCell>
                                        <TableCell align="right">{row.date}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                </Paper>
            </Grid>
        </Box>
    );
};

export default Body;