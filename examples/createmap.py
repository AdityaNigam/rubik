#!/usr/bin/env python2.6
################################################################################
# Copyright (c) 2012, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory
# Written by Todd Gamblin et al. <tgamblin@llnl.gov>
# LLNL-CODE-599252
# All rights reserved.
# 
# This file is part of Rubik. For details, see http://scalability.llnl.gov.
# Please read the LICENSE file for further information.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the disclaimer below.
# 
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the disclaimer (as noted below) in the
#       documentation and/or other materials provided with the distribution.
# 
#     * Neither the name of the LLNS/LLNL nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL LAWRENCE LIVERMORE NATIONAL SECURITY, LLC, THE
# U.S. DEPARTMENT OF ENERGY OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
################################################################################

from rubik import *

# application topology
app = box([8, 8])
app.tile([4, 4])
print app
print ""

# processor topology
torus = box([4, 4, 4])
torus.tile([1, 4, 4])

torus.map(app)
print torus
print ""

f = open('mapfile', 'w')
torus.write_map_file(f)
f.close()
