# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, absolute_import)

import logging
from functools import partial
import six

from django.utils.translation import ugettext_lazy as _
from julia import node, shortcuts

from . import const

logger = logging.getLogger(__name__)

# aquire a stream pattern node that will live in memory 
# and will be available application wide
try:
    stream_pattern_node = shortcuts.parse_pattern(const.STREAM_PATTERN)
except node.PatternNodeError as e:
    logger.critical('failed to parse pattern ({})'.format(e))
    raise

unmap = partial(shortcuts.unmap, coerce=int)

# list of (rank name, points required to earn the rank) tuples
RANKS = (
    (_('Cadet'), 0),
    (_('Patrol Officer'), 500),
    (_('Reserve Officer'), 1000),
    (_('Lance Corporal'), 2000),
    (_('Corporal'), 3000),
    (_('Sergeant'), 4000),
    (_('First Sergeant'), 5000),

    (_('Lieutenant'), 10000),
    (_('Captain'), 15000),
    (_('Major'), 20000),

    (_('Deputy Chief'), 30000),
    (_('Assistant Chief'), 40000),
    (_('Chief of Police'), 50000),
)

# stat id -> human readable name mapping
# used everywhere across the app
STATS = {
    const.STATS_SCORE: 'score',
    const.STATS_TIME: 'time',
    const.STATS_KILLS: 'kills',
    const.STATS_TEAMKILLS: 'teamkills',
    const.STATS_DEATHS: 'deaths',
    const.STATS_SUICIDES: 'suicides',
    const.STATS_ARRESTS: 'arrests',
    const.STATS_ARRESTED: 'arrested',
    const.STATS_KILL_STREAK: 'kill_streak',
    const.STATS_ARREST_STREAK: 'arrest_streak',
    const.STATS_DEATH_STREAK: 'death_streak',
    const.STATS_VIP_CAPTURES: 'vip_captures',
    const.STATS_VIP_RESCUES: 'vip_rescues',
    const.STATS_VIP_ESCAPES: 'vip_escapes',
    const.STATS_VIP_KILLS_VALID: 'vip_kills_valid',
    const.STATS_VIP_KILLS_INVALID: 'vip_kills_invalid',
    const.STATS_RD_BOMBS_DEFUSED: 'rd_bombs_defused',
    const.STATS_SG_ESCAPES: 'sg_escapes',
    const.STATS_SG_KILLS: 'sg_kills',
    const.STATS_COOP_HOSTAGE_ARRESTS: 'coop_hostage_arrests',
    const.STATS_COOP_HOSTAGE_HITS: 'coop_hostage_hits',
    const.STATS_COOP_HOSTAGE_INCAPS: 'coop_hostage_incaps',
    const.STATS_COOP_HOSTAGE_KILLS: 'coop_hostage_kills',
    const.STATS_COOP_ENEMY_ARRESTS: 'coop_enemy_arrests',
    const.STATS_COOP_ENEMY_INCAPS: 'coop_enemy_incaps',
    const.STATS_COOP_ENEMY_KILLS: 'coop_enemy_kills',
    const.STATS_COOP_ENEMY_INCAPS_INVALID: 'coop_enemy_incaps_invalid',
    const.STATS_COOP_ENEMY_KILLS_INVALID: 'coop_enemy_kills_invalid',
    const.STATS_COOP_TOC_REPORTS: 'coop_toc_reports',
    # extra
    const.STATS_TOP_SCORE: 'top_score',
    const.STATS_TOP_KILLS: 'top_kills',
    const.STATS_TOP_ARRESTS: 'top_arrests',
    const.STATS_SPM: 'spm',
    const.STATS_SPR: 'spr',
    const.STATS_KDR: 'kdr',
    const.STATS_GAMES: 'games',
    const.STATS_WINS: 'wins',
    const.STATS_LOSSES: 'losses',
    const.STATS_DRAWS: 'draws',
    # weapons
    const.STATS_AMMO_SHOTS: 'ammo_shots',
    const.STATS_AMMO_HITS: 'ammo_hits',
    const.STATS_AMMO_ACCURACY: 'ammo_accuracy',
    const.STATS_AMMO_DISTANCE: 'ammo_distance',
    # coop extra
    const.STATS_COOP_SCORE: 'coop_score',
    const.STATS_COOP_TEAMKILLS: 'coop_teamkills',
    const.STATS_COOP_DEATHS: 'coop_deaths',
    const.STATS_COOP_GAMES: 'coop_games',
    const.STATS_COOP_TIME: 'coop_time',
    const.STATS_COOP_WINS: 'coop_wins',
    const.STATS_COOP_LOSSES: 'coop_losses',
}

# inverse the mapping (e.g. score -> 0)
STATS_INVERSED = dict((v, k) for k, v in six.iteritems(STATS))

# translate the lethal and thrown weapon names 
# into a sequence of the corresponding numeric keys
# The list is used to calculate overall accuracy
WEAPONS_FIRED = unmap(
    stream_pattern_node.item('players').item, 'loadout__primary', (
        'M4 Super90',
        'Nova Pump',
        'Shotgun',
        #'Less Lethal Shotgun',
        #'Pepper-ball',
        'Colt M4A1 Carbine',
        'AK-47 Machinegun',
        'GB36s Assault Rifle',
        'Gal Sub-machinegun',
        '9mm SMG',
        'Suppressed 9mm SMG',
        '.45 SMG',
        'M1911 Handgun',
        '9mm Handgun',
        'Colt Python',
        #'Taser Stun Gun',
        'VIP Colt M1911 Handgun',
        'Colt Accurized Rifle',
        #'40mm Grenade Launcher',
        '5.56mm Light Machine Gun',
        '5.7x28mm Submachine Gun',
        'Mark 19 Semi-Automatic Pistol',
        '9mm Machine Pistol',
        #'Cobra Stun Gun',
        #'Baton',
    )
)

WEAPONS_THROWN = unmap(
    stream_pattern_node.item('players').item, 'loadout__primary', (
        'Stinger',
        'CS Gas',
        'Flashbang',
    )
)

WEAPONS_PRIMARY = unmap(
    stream_pattern_node.item('players').item, 'loadout__primary', (
        'M4 Super90',
        'Nova Pump',
        'Pepper-ball',
        'Less Lethal Shotgun',
        'Colt M4A1 Carbine',
        'AK-47 Machinegun',
        'GB36s Assault Rifle',
        'Gal Sub-machinegun',
        '9mm SMG',
        'Suppressed 9mm SMG',
        '.45 SMG',
        'Colt Accurized Rifle',
        '40mm Grenade Launcher',
        '5.56mm Light Machine Gun',
        '5.7x28mm Submachine Gun',
        '9mm Machine Pistol',
    )
)

WEAPONS_SECONDARY = unmap(
    stream_pattern_node.item('players').item, 'loadout__primary', (
        'Taser Stun Gun',
        'Cobra Stun Gun',
        'M1911 Handgun',
        '9mm Handgun',
        'Colt Python',
        'VIP Colt M1911 Handgun',
        'Mark 19 Semi-Automatic Pistol',
    )
)

WEAPONS_TACTICAL = unmap(
    stream_pattern_node.item('players').item, 'loadout__primary', (
        'Pepper Spray',
        'Stinger',
        #'CS Gas',
        'Flashbang',
        'Shotgun',
        'Zip-cuffs',
        'Optiwand',
    )
)

TEAM_BLUE = unmap(stream_pattern_node.item('players').item, 'team', 'swat')
TEAM_RED = unmap(stream_pattern_node.item('players').item, 'team', 'suspects')

MODE_BS = unmap(stream_pattern_node, 'gametype', 'Barricaded Suspects')
MODE_VIP = unmap(stream_pattern_node, 'gametype', 'VIP Escort')
MODE_RD = unmap(stream_pattern_node, 'gametype', 'Rapid Deployment')
MODE_SG = unmap(stream_pattern_node, 'gametype', 'Smash And Grab')

MODES_VERSUS = (MODE_BS, MODE_VIP, MODE_RD, MODE_SG)
MODES_COOP = unmap(stream_pattern_node, 'gametype', ('CO-OP',))  # 'CO-OP QMM'?
MODES_ALL = MODES_VERSUS + MODES_COOP

# Outcome indicating a swat victory in a game
SWAT_GAMES = unmap(
    stream_pattern_node, 'outcome', ('swat_bs', 'swat_rd', 'swat_vip_escape', 'swat_vip_bad_kill', 'swat_sg')
)
# Outcome indicating a suspects victory in a game
SUS_GAMES = unmap(
    stream_pattern_node, 'outcome', ('sus_bs', 'sus_rd', 'sus_vip_good_kill', 'sus_vip_bad_kill', 'sus_sg')
)
# A tie outcome
DRAW_GAMES = unmap(
    stream_pattern_node, 'outcome', ('tie',)
)
# COOP completed outcome
COMPLETED_MISSIONS = unmap(
    stream_pattern_node, 'outcome', ('coop_completed',)
)
# COOP failed outcome
FAILED_MISSIONS = unmap(
    stream_pattern_node, 'outcome', ('coop_failed',)
)

# COOP objective completed status
OBJECTIVE_COMPLETED = unmap(
    stream_pattern_node.item('coop_objectives').item, 'status', 'completed'
)

# COOP objective failed status
OBJECTIVE_FAILED = unmap(
    stream_pattern_node.item('coop_objectives').item, 'status', 'failed'
)

PATTERN_IPV4 = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
PATTERN_PORT = r'\d{1,5}'