# -*- coding: utf-8 -*-
from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital2.hospital'
    _description = 'hospital.hospital'

    name = fields.Char(
    string='Name',
    required=True
    )
    age = fields.Integer(
    string='Age'
    )
    is_child  = fields.Boolean(
    string='Is child?'
    )
    notes  = fields.Text(
    string='Notes'
    )
    gender  = fields.Selection([('male', 'Male'),('female', 'Female'),('others', 'Others')],
    string='Gender'
    )
    #1st is key 2nd the value
 

 

