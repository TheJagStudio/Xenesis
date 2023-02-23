window.addEventListener("app:mounted", (function() {
    new Tab("#sales-tab");
    var e = {
            colors: ["#4467EF"],
            chart: {
                height: 60,
                type: "line",
                parentHeightOffset: 0,
                toolbar: {
                    show: !1
                }
            },
            series: [{
                name: "Sales",
                data: [654, 820, 102, 540, 154, 614]
            }],
            dataLabels: {
                enabled: !1
            },
            stroke: {
                curve: "smooth",
                width: 3
            },
            grid: {
                padding: {
                    left: 0,
                    right: 0,
                    top: -20,
                    bottom: -10
                }
            },
            xaxis: {
                show: !1,
                axisBorder: {
                    show: !1
                },
                axisTicks: {
                    show: !1
                },
                labels: {
                    show: !1
                }
            },
            yaxis: {
                show: !1,
                axisBorder: {
                    show: !1
                },
                axisTicks: {
                    show: !1
                },
                labels: {
                    show: !1
                }
            }
        },
        o = document.querySelector("#salesMonthChart");
    setTimeout((function() {
        o._chart = new ApexCharts(o, e), o._chart.render()
    }));
    var t = {
            colors: ["#4C4EE7", "#0EA5E9"],
            series: [{
                name: "Sales",
                data: [28, 45, 35, 50, 32]
            }, {
                name: "Profit",
                data: [14, 25, 20, 25, 12]
            }],
            chart: {
                height: 255,
                type: "bar",
                parentHeightOffset: 0,
                toolbar: {
                    show: !1
                }
            },
            dataLabels: {
                enabled: !1
            },
            plotOptions: {
                bar: {
                    borderRadius: 4,
                    barHeight: "90%",
                    columnWidth: "35%"
                }
            },
            legend: {
                show: !1
            },
            xaxis: {
                categories: ["Week1", "Week2", "Week3", "Week4", "Week5", "Week6"],
                labels: {
                    hideOverlappingLabels: !1
                },
                axisBorder: {
                    show: !1
                },
                axisTicks: {
                    show: !1
                },
                tooltip: {
                    enabled: !1
                }
            },
            grid: {
                padding: {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: -10
                }
            },
            yaxis: {
                show: !1,
                axisBorder: {
                    show: !1
                },
                axisTicks: {
                    show: !1
                },
                labels: {
                    show: !1
                }
            },
            responsive: [{
                breakpoint: 850,
                options: {
                    plotOptions: {
                        bar: {
                            columnWidth: "55%"
                        }
                    }
                }
            }]
        },
        a = document.querySelector("#salesOverview");
    setTimeout((function() {
        a._chart = new ApexCharts(a, t), a._chart.render()
    })), bandwidthConfig = {
        colors: ["#4467EF"],
        series: [{
            name: "Traffic",
            data: [8107.85, 8128, 8122.9, 8165.5, 8340.7, 8423.7, 8423.5, 8514.3, 8481.85, 8487.7, 8506.9, 8626.2, 8668.95, 8602.3, 8607.55, 8512.9, 8496.25, 8600.65, 8881.1, 9340.85]
        }],
        chart: {
            type: "area",
            height: 220,
            parentHeightOffset: 0,
            toolbar: {
                show: !1
            },
            zoom: {
                enabled: !1
            }
        },
        dataLabels: {
            enabled: !1
        },
        stroke: {
            curve: "smooth",
            width: 2
        },
        grid: {
            padding: {
                left: 0,
                right: 0,
                top: -28,
                bottom: -15
            }
        },
        tooltip: {
            shared: !0
        },
        legend: {
            show: !1
        },
        yaxis: {
            show: !1
        },
        xaxis: {
            labels: {
                show: !1
            },
            axisTicks: {
                show: !1
            },
            axisBorder: {
                show: !1
            }
        }
    };
    var r = document.querySelector("#bandwidth-chart");
    setTimeout((function() {
        r._chart = new ApexCharts(r, bandwidthConfig), r._chart.render()
    }));
    var s = {
        placement: "bottom-end",
        modifiers: [{
            name: "offset",
            options: {
                offset: [0, 4]
            }
        }]
    };
    new Popper("#project-status-menu", ".popper-ref", ".popper-root", s), new Popper("#satisfaction-menu", ".popper-ref", ".popper-root", s), new Popper("#bandwidth-menu", ".popper-ref", ".popper-root", s), new Popper("#users-activity-menu", ".popper-ref", ".popper-root", s)
}), {
    once: !0
});