from datetime import date, timedelta
aktivitate = {b'resource_state': 2, b'athlete': {'id': 64810102, 'resource_state': 1},
               b'name': b'Afternoon Run', b'distance': 4430.7, b'moving_time': 2280,
                 b'elapsed_time': 2294, b'total_elevation_gain': 15.2, b'type': b'Run',
                   b'sport_type': b'Run', b'workout_type': None, b'id': 4626206245,
                     b'start_date': b'2020-10-20T14:21:50Z', b'start_date_local': b'2020-10-20T17:21:50Z', b'timezone': b'(GMT+02:00) Europe/Riga',
                       b'utc_offset': 10800.0, b'location_city': None, b'location_state': None, b'location_country': None, b'achievement_count': 0,
                         b'kudos_count': 0, b'comment_count': 0, b'athlete_count': 1, b'photo_count': 0, b'map': {'id': 'a4626206245',
                             'summary_polyline': '}|w|IcjmyCWFa@CoCq@wBYoFkAoA]c@O_Ci@Wc@HwAVkCr@cDPiAH{BGsDYmEg@sEIwBWwBQwDKwD@eAAkA@wHHe@Pe@@s@Jq@CSWeAM{@K_CB{@AcE@wCB_A?{BDiD?a@DkACwDFuJHcC?qFB_BBeCHu@FChAg@f@Y|@Q`@G`A?~BE~@IdAFTHVD~@CRA`@Sr@y@~@yANQpAgAdAa@^E`ANt@DVHzAJl@J|@p@HJf@`@Rj@s@bGG`A[pAGp@U`AW~AOpAMbBa@hCCl@c@bEGbAOz@MhAK\\QpAS~@WbDa@xJa@bFa@lIIfCGn@EdAGj@GpB_@dGG~BOdC@XIr@OxDGjB?nCQ~GA`BBf@IbE@`@ACCB?`BBl@?bFBv@CZ', 'resource_state': 2},
                               b'trainer': False, b'commute': False, b'manual': False, b'private': False, b'visibility': b'everyone', b'flagged': False,
                                 b'gear_id': None, b'start_latlng': [57.30783, 25.304823], b'end_latlng': [57.307764, 25.305032], b'average_speed': 1.943,
                                   b'max_speed': 2.7, b'average_cadence': 70.5, b'has_heartrate': False, b'heartrate_opt_out': False, b'display_hide_heartrate_option': False,
                                     b'elev_high': 127.9, b'elev_low': 118.9, b'upload_id': 4941109614, b'upload_id_str': b'4941109614', b'external_id': b'stripped_health_data_64810102_1610745870.gpx',
                                       b'from_accepted_tag': False, b'pr_count': 0, b'total_photo_count': 0, b'has_kudoed': False}
otra = {b'resource_state': 2, b'athlete': {'id': 64810102, 'resource_state': 1},
               b'name': b'Afternoon Run', b'distance': 4430.7, b'moving_time': 2280,
                 b'elapsed_time': 2294, b'total_elevation_gain': 15.2, b'type': b'Run',
                   b'sport_type': b'Run', b'workout_type': None, b'id': 4626206245,
                     b'start_date': b'2020-10-20T14:21:50Z', b'start_date_local': b'2020-10-21T17:21:50Z', b'timezone': b'(GMT+02:00) Europe/Riga',
                       b'utc_offset': 10800.0, b'location_city': None, b'location_state': None, b'location_country': None, b'achievement_count': 0,
                         b'kudos_count': 0, b'comment_count': 0, b'athlete_count': 1, b'photo_count': 0, b'map': {'id': 'a4626206245',
                             'summary_polyline': '}|w|IcjmyCWFa@CoCq@wBYoFkAoA]c@O_Ci@Wc@HwAVkCr@cDPiAH{BGsDYmEg@sEIwBWwBQwDKwD@eAAkA@wHHe@Pe@@s@Jq@CSWeAM{@K_CB{@AcE@wCB_A?{BDiD?a@DkACwDFuJHcC?qFB_BBeCHu@FChAg@f@Y|@Q`@G`A?~BE~@IdAFTHVD~@CRA`@Sr@y@~@yANQpAgAdAa@^E`ANt@DVHzAJl@J|@p@HJf@`@Rj@s@bGG`A[pAGp@U`AW~AOpAMbBa@hCCl@c@bEGbAOz@MhAK\\QpAS~@WbDa@xJa@bFa@lIIfCGn@EdAGj@GpB_@dGG~BOdC@XIr@OxDGjB?nCQ~GA`BBf@IbE@`@ACCB?`BBl@?bFBv@CZ', 'resource_state': 2},
                               b'trainer': False, b'commute': False, b'manual': False, b'private': False, b'visibility': b'everyone', b'flagged': False,
                                 b'gear_id': None, b'start_latlng': [57.30783, 25.304823], b'end_latlng': [57.307764, 25.305032], b'average_speed': 1.943,
                                   b'max_speed': 2.7, b'average_cadence': 70.5, b'has_heartrate': False, b'heartrate_opt_out': False, b'display_hide_heartrate_option': False,
                                     b'elev_high': 127.9, b'elev_low': 118.9, b'upload_id': 4941109614, b'upload_id_str': b'4941109614', b'external_id': b'stripped_health_data_64810102_1610745870.gpx',
                                       b'from_accepted_tag': False, b'pr_count': 0, b'total_photo_count': 0, b'has_kudoed': False}
visas = [aktivitate, otra]
sodiena = date.today()
laiks = "7"
print(visas[1]["start_date_local"].decode("utf-8"))
print(sodiena)
for k in visas:
    if laiks == "7":
        datums = sodiena - timedelta(days=7)
    start_datums = k['start_date_local'].decode("utf-8")
    a_datums, parejais = k["start_date_local"].split("T")