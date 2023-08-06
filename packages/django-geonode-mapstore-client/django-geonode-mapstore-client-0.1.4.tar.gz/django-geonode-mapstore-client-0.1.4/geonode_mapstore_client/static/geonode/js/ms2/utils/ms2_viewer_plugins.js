var MS2_PLUGINS = {
	"desktop": [{
			"name": "Map",
			"cfg": {
				"tools": ["locate", "measurement"],
				"mapOptions": {
					"openlayers": {
						"interactions": {
							"pinchRotate": false,
							"altShiftDragRotate": false
						}
					},
					"leaflet": {
						"attribution": {
							"container": "#mapstore-map-footer-container"
						}
					}
				}
			}
		}, {
			"name": "DrawerMenu"
		}, {
			"name": "BackgroundSelector",
			"cfg": {
				"style": {
					"bottom": 0,
					"marginBottom": 30
				},
				"dimensions": {
					"side": 65,
					"sidePreview": 65,
					"frame": 3,
					"margin": 5,
					"label": false,
					"vertical": false
				}
			}
		},
		{
			"name": "Identify",
			"cfg": {
				"showFullscreen": false,
				"dock": false,
				"position": "bottom",
				"size": 0.5,
				"fluid": true,
				"viewerOptions": {
					"container": "{context.ReactSwipe}"
				}
			},
			"override": {
				"Toolbar": {
					"position": 11,
					"alwaysVisible": false
				}
			}
		}, {
			"name": "ZoomAll",
			"override": {
				"Toolbar": {
					"alwaysVisible": false
				}
			}
		}, {
			"name": "TOC",
			"cfg": {
				"activateMapTitle": false,
				"activateSettingsTool": false,
				"activateMetedataTool": false,
				"activateRemoveLayer": false
			}

		}, {
			"name": "Settings",
			"cfg": {
				"wrap": true
			}
		}, {
			"name": "Toolbar",
			"id": "NavigationBar",
			"cfg": {
				"id": "navigationBar",
				"layout": "horizontal"
			}
		}, {
			"name": "MapLoading",
			"override": {
				"Toolbar": {
					"alwaysVisible": true
				}
			}
		}, "Cookie",
		"OmniBar", {
			"name": "GoFull",
			"override": {
				"Toolbar": {
					"alwaysVisible": false
				}
			}
		},
		"Expander", "ScaleBox", "Undo", "Redo",
		{
			"name": "FullScreen",
			"override": {
				"Toolbar": {
					"alwaysVisible": false
				}
			}
		},
        "BurgerMenu",
        "MapFooter",
        {
			"name": "Print",
			"cfg": {
				"useFixedScales": true,
                "mapPreviewOptions": {
                    "enableScalebox": true,
                    "enableRefresh": false
                }
			}
		},
		{
			"name": "ZoomIn",
			"override": {
				"Toolbar": {
					"alwaysVisible": true
				}
			}
		}, {
			"name": "Measure"
		}, {
			"name": "ZoomOut",
			"override": {
				"Toolbar": {
					"alwaysVisible": true
				}
			}
		}
	]
}
