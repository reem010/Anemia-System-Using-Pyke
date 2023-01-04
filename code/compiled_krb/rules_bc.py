# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def no_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.no_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.no_anemia: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mild1_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.mild1_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.mild1_anemia: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mild2_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.mild2_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.mild2_anemia: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def full_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.full_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.full_anemia: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron1_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron1_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron1_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron1_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,2,3,4,5):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron2_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron2_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron2_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron2_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,2,3,4,5)      :
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron3_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron3_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron3_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron3_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,2,3,4,5)        :
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron4_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron4_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron4_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron4_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (6,)      :
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron5_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron5_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron5_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron5_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (6,)        :
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron6_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron6_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron6_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron6_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (6,)        :
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron7_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron7_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron7_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron7_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.iron7_anemia: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron8_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron8_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron8_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron8_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.iron8_anemia: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron9_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron9_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron9_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron9_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.iron9_anemia: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron10_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron10_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron10_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron10_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.iron10_anemia: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron11_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron11_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron11_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron11_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.iron11_anemia: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def iron12_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.iron12_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.iron12_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.iron12_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.iron12_anemia: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic1_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic1_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic1_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic1_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic1_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic1_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (1,2,3,4):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic2_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic2_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic2_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic2_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic2_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic2_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (1,2,3,4):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic3_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic3_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic3_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic3_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic3_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic3_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (1,2,3,4):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic4_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic4_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic4_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic4_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic4_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic4_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (5,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic5_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic5_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic5_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic5_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic5_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic5_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (5,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic6_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic6_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic6_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic6_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic6_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic6_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (5,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic7_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic7_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic7_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic7_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic7_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic7_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (6,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic8_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic8_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic8_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic8_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic8_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic8_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (6,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def folic9_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.folic9_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.folic9_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.folic9_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.folic9_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.folic9_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('test') in (6,):
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia1_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia1_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia1_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia1_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia1_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia1_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia1_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (1,2,3,4,5):
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia2_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia2_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia2_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia2_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia2_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia2_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia2_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (1,2,3,4,5)   :
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia3_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia3_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia3_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia3_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia3_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia3_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia3_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (1,2,3,4,5)  :
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia4_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia4_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia4_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia4_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia4_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia4_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia4_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (6,) :
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia5_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia5_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia5_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia5_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia5_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia5_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia5_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (6,) :
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia6_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia6_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia6_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia6_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia6_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia6_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia6_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (6,)         :
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia7_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia7_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia7_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia7_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia7_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia7_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia7_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (7,):
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia8_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia8_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia8_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia8_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia8_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia8_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia8_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (7,):
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Thalassemia9_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Thalassemia9_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Thalassemia9_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Thalassemia9_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Thalassemia9_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Thalassemia9_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Thalassemia9_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('test') in (7,):
                                      rule.rule_base.num_bc_rule_successes += 1
                                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi1_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi1_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi1_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi1_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi1_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi1_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi1_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi1_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (1,2,3,4,5):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi2_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi2_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi2_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi2_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi2_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi2_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi2_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi2_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (1,2,3,4,5):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi3_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi3_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi3_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi3_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi3_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi3_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi3_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi3_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (1,2,3,4,5):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi4_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi4_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi4_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi4_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi4_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi4_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi4_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi4_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (6,):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi5_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi5_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi5_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi5_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi5_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi5_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi5_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi5_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (6,):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi6_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi6_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi6_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi6_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi6_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi6_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi6_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi6_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (6,):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi7_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi7_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi7_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi7_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi7_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi7_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi7_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi7_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (7,):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi8_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi8_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi8_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi8_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(1),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi8_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi8_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi8_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi8_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (7,):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fanconi9_anemia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_fatigue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.Fanconi9_anemia: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_pallor', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.Fanconi9_anemia: got unexpected plan from when clause 2"
                with engine.prove('questions', 'Iron_Deficiency', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.Fanconi9_anemia: got unexpected plan from when clause 3"
                    if context.lookup_data('iron') in (7,):
                      with engine.prove('questions', 'is_ironfood', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.Fanconi9_anemia: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'Folic_Deficiency', context,
                                            (rule.pattern(3),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.Fanconi9_anemia: got unexpected plan from when clause 6"
                              if context.lookup_data('folic') in (6,):
                                with engine.prove('questions', 'Thalassemia_Deficiency', context,
                                                  (rule.pattern(4),)) \
                                  as gen_8:
                                  for x_8 in gen_8:
                                    assert x_8 is None, \
                                      "rules.Fanconi9_anemia: got unexpected plan from when clause 8"
                                    if context.lookup_data('thalassemia') in (7,):
                                      with engine.prove('questions', 'Fanconi_Anemia', context,
                                                        (rule.pattern(5),)) \
                                        as gen_10:
                                        for x_10 in gen_10:
                                          assert x_10 is None, \
                                            "rules.Fanconi9_anemia: got unexpected plan from when clause 10"
                                          if context.lookup_data('fanconi') in (7,):
                                            rule.rule_base.num_bc_rule_successes += 1
                                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('no_anemia', This_rule_base, 'what_to_bring',
                  no_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Anemia'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('mild1_anemia', This_rule_base, 'what_to_bring',
                  mild1_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('mild2_anemia', This_rule_base, 'what_to_bring',
                  mild2_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Anemia'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('full_anemia', This_rule_base, 'what_to_bring',
                  full_anemia, None,
                  (pattern.pattern_literal('You_Have_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('iron1_anemia', This_rule_base, 'what_to_bring',
                  iron1_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron2_anemia', This_rule_base, 'what_to_bring',
                  iron2_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron3_anemia', This_rule_base, 'what_to_bring',
                  iron3_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron4_anemia', This_rule_base, 'what_to_bring',
                  iron4_anemia, None,
                  (pattern.pattern_literal('You_Have_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron5_anemia', This_rule_base, 'what_to_bring',
                  iron5_anemia, None,
                  (pattern.pattern_literal('You_Have_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron6_anemia', This_rule_base, 'what_to_bring',
                  iron6_anemia, None,
                  (pattern.pattern_literal('You_Have_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron7_anemia', This_rule_base, 'what_to_bring',
                  iron7_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron8_anemia', This_rule_base, 'what_to_bring',
                  iron8_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron9_anemia', This_rule_base, 'what_to_bring',
                  iron9_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron10_anemia', This_rule_base, 'what_to_bring',
                  iron10_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('iron11_anemia', This_rule_base, 'what_to_bring',
                  iron11_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('iron12_anemia', This_rule_base, 'what_to_bring',
                  iron12_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Iron_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('folic1_anemia', This_rule_base, 'what_to_bring',
                  folic1_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic2_anemia', This_rule_base, 'what_to_bring',
                  folic2_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic3_anemia', This_rule_base, 'what_to_bring',
                  folic3_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic4_anemia', This_rule_base, 'what_to_bring',
                  folic4_anemia, None,
                  (pattern.pattern_literal('You_Have_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic5_anemia', This_rule_base, 'what_to_bring',
                  folic5_anemia, None,
                  (pattern.pattern_literal('You_Have_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic6_anemia', This_rule_base, 'what_to_bring',
                  folic6_anemia, None,
                  (pattern.pattern_literal('You_Have_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic7_anemia', This_rule_base, 'what_to_bring',
                  folic7_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic8_anemia', This_rule_base, 'what_to_bring',
                  folic8_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('folic9_anemia', This_rule_base, 'what_to_bring',
                  folic9_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Folic_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia1_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia1_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   pattern.pattern_literal(False),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia2_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia2_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia3_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia3_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia4_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia4_anemia, None,
                  (pattern.pattern_literal('You_Have_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   pattern.pattern_literal(False),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia5_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia5_anemia, None,
                  (pattern.pattern_literal('You_Have_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia6_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia6_anemia, None,
                  (pattern.pattern_literal('You_Have_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia7_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia7_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   pattern.pattern_literal(False),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia8_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia8_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Thalassemia9_anemia', This_rule_base, 'what_to_bring',
                  Thalassemia9_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Thalassemia_Acid_Deficiency'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('test'),))
  
  bc_rule.bc_rule('Fanconi1_anemia', This_rule_base, 'what_to_bring',
                  Fanconi1_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   pattern.pattern_literal(False),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi2_anemia', This_rule_base, 'what_to_bring',
                  Fanconi2_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi3_anemia', This_rule_base, 'what_to_bring',
                  Fanconi3_anemia, None,
                  (pattern.pattern_literal('You_Have_Mild_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi4_anemia', This_rule_base, 'what_to_bring',
                  Fanconi4_anemia, None,
                  (pattern.pattern_literal('You_Have_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   pattern.pattern_literal(False),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi5_anemia', This_rule_base, 'what_to_bring',
                  Fanconi5_anemia, None,
                  (pattern.pattern_literal('You_Have_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi6_anemia', This_rule_base, 'what_to_bring',
                  Fanconi6_anemia, None,
                  (pattern.pattern_literal('You_Have_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi7_anemia', This_rule_base, 'what_to_bring',
                  Fanconi7_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   pattern.pattern_literal(False),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi8_anemia', This_rule_base, 'what_to_bring',
                  Fanconi8_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))
  
  bc_rule.bc_rule('Fanconi9_anemia', This_rule_base, 'what_to_bring',
                  Fanconi9_anemia, None,
                  (pattern.pattern_literal('You_Have_No_Fanconi_Anemia'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('iron'),
                   contexts.variable('folic'),
                   contexts.variable('thalassemia'),
                   contexts.variable('fanconi'),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 25), (7, 7)),
    ((26, 31), (8, 8)),
    ((44, 48), (11, 11)),
    ((50, 55), (13, 13)),
    ((56, 61), (14, 14)),
    ((74, 78), (17, 17)),
    ((80, 85), (19, 19)),
    ((86, 91), (20, 20)),
    ((104, 108), (23, 23)),
    ((110, 115), (25, 25)),
    ((116, 121), (26, 26)),
    ((134, 138), (32, 32)),
    ((140, 145), (34, 34)),
    ((146, 151), (35, 35)),
    ((152, 157), (36, 36)),
    ((158, 158), (37, 37)),
    ((171, 175), (41, 41)),
    ((177, 182), (43, 43)),
    ((183, 188), (44, 44)),
    ((189, 194), (45, 45)),
    ((195, 195), (46, 46)),
    ((208, 212), (49, 49)),
    ((214, 219), (51, 51)),
    ((220, 225), (52, 52)),
    ((226, 231), (53, 53)),
    ((232, 232), (54, 54)),
    ((245, 249), (59, 59)),
    ((251, 256), (61, 61)),
    ((257, 262), (62, 62)),
    ((263, 268), (63, 63)),
    ((269, 269), (64, 64)),
    ((282, 286), (68, 68)),
    ((288, 293), (70, 70)),
    ((294, 299), (71, 71)),
    ((300, 305), (72, 72)),
    ((306, 306), (73, 73)),
    ((319, 323), (76, 76)),
    ((325, 330), (78, 78)),
    ((331, 336), (79, 79)),
    ((337, 342), (80, 80)),
    ((343, 343), (81, 81)),
    ((356, 360), (86, 86)),
    ((362, 367), (88, 88)),
    ((368, 373), (89, 89)),
    ((374, 379), (90, 90)),
    ((380, 380), (91, 91)),
    ((381, 386), (92, 92)),
    ((399, 403), (95, 95)),
    ((405, 410), (97, 97)),
    ((411, 416), (98, 98)),
    ((417, 422), (99, 99)),
    ((423, 423), (100, 100)),
    ((424, 429), (101, 101)),
    ((442, 446), (104, 104)),
    ((448, 453), (106, 106)),
    ((454, 459), (107, 107)),
    ((460, 465), (108, 108)),
    ((466, 466), (109, 109)),
    ((467, 472), (110, 110)),
    ((485, 489), (113, 113)),
    ((491, 496), (115, 115)),
    ((497, 502), (116, 116)),
    ((503, 508), (117, 117)),
    ((509, 509), (118, 118)),
    ((510, 515), (119, 119)),
    ((528, 532), (123, 123)),
    ((534, 539), (125, 125)),
    ((540, 545), (126, 126)),
    ((546, 551), (127, 127)),
    ((552, 552), (128, 128)),
    ((553, 558), (129, 129)),
    ((571, 575), (134, 134)),
    ((577, 582), (136, 136)),
    ((583, 588), (137, 137)),
    ((589, 594), (138, 138)),
    ((595, 595), (139, 139)),
    ((596, 601), (140, 140)),
    ((614, 618), (145, 145)),
    ((620, 625), (147, 147)),
    ((626, 631), (148, 148)),
    ((632, 637), (149, 149)),
    ((638, 638), (150, 150)),
    ((639, 644), (151, 151)),
    ((645, 650), (152, 152)),
    ((651, 651), (153, 153)),
    ((664, 668), (156, 156)),
    ((670, 675), (158, 158)),
    ((676, 681), (159, 159)),
    ((682, 687), (160, 160)),
    ((688, 688), (161, 161)),
    ((689, 694), (162, 162)),
    ((695, 700), (163, 163)),
    ((701, 701), (164, 164)),
    ((714, 718), (167, 167)),
    ((720, 725), (169, 169)),
    ((726, 731), (170, 170)),
    ((732, 737), (171, 171)),
    ((738, 738), (172, 172)),
    ((739, 744), (173, 173)),
    ((745, 750), (174, 174)),
    ((751, 751), (175, 175)),
    ((764, 768), (179, 179)),
    ((770, 775), (181, 181)),
    ((776, 781), (182, 182)),
    ((782, 787), (183, 183)),
    ((788, 788), (184, 184)),
    ((789, 794), (185, 185)),
    ((795, 800), (186, 186)),
    ((801, 801), (187, 187)),
    ((814, 818), (191, 191)),
    ((820, 825), (193, 193)),
    ((826, 831), (194, 194)),
    ((832, 837), (195, 195)),
    ((838, 838), (196, 196)),
    ((839, 844), (197, 197)),
    ((845, 850), (198, 198)),
    ((851, 851), (199, 199)),
    ((864, 868), (202, 202)),
    ((870, 875), (204, 204)),
    ((876, 881), (205, 205)),
    ((882, 887), (206, 206)),
    ((888, 888), (207, 207)),
    ((889, 894), (208, 208)),
    ((895, 900), (209, 209)),
    ((901, 901), (210, 210)),
    ((914, 918), (213, 213)),
    ((920, 925), (215, 215)),
    ((926, 931), (216, 216)),
    ((932, 937), (217, 217)),
    ((938, 938), (218, 218)),
    ((939, 944), (219, 219)),
    ((945, 950), (220, 220)),
    ((951, 951), (221, 221)),
    ((964, 968), (225, 225)),
    ((970, 975), (227, 227)),
    ((976, 981), (228, 228)),
    ((982, 987), (229, 229)),
    ((988, 988), (230, 230)),
    ((989, 994), (231, 231)),
    ((995, 1000), (232, 232)),
    ((1001, 1001), (233, 233)),
    ((1014, 1018), (236, 236)),
    ((1020, 1025), (238, 238)),
    ((1026, 1031), (239, 239)),
    ((1032, 1037), (240, 240)),
    ((1038, 1038), (241, 241)),
    ((1039, 1044), (242, 242)),
    ((1045, 1050), (243, 243)),
    ((1051, 1051), (244, 244)),
    ((1064, 1068), (249, 249)),
    ((1070, 1075), (251, 251)),
    ((1076, 1081), (252, 252)),
    ((1082, 1087), (253, 253)),
    ((1088, 1088), (254, 254)),
    ((1089, 1094), (255, 255)),
    ((1095, 1100), (256, 256)),
    ((1101, 1101), (257, 257)),
    ((1102, 1107), (258, 258)),
    ((1108, 1108), (259, 259)),
    ((1121, 1125), (262, 262)),
    ((1127, 1132), (264, 264)),
    ((1133, 1138), (265, 265)),
    ((1139, 1144), (266, 266)),
    ((1145, 1145), (267, 267)),
    ((1146, 1151), (268, 268)),
    ((1152, 1157), (269, 269)),
    ((1158, 1158), (270, 270)),
    ((1159, 1164), (271, 271)),
    ((1165, 1165), (272, 272)),
    ((1178, 1182), (275, 275)),
    ((1184, 1189), (277, 277)),
    ((1190, 1195), (278, 278)),
    ((1196, 1201), (279, 279)),
    ((1202, 1202), (280, 280)),
    ((1203, 1208), (281, 281)),
    ((1209, 1214), (282, 282)),
    ((1215, 1215), (283, 283)),
    ((1216, 1221), (284, 284)),
    ((1222, 1222), (285, 285)),
    ((1235, 1239), (288, 288)),
    ((1241, 1246), (290, 290)),
    ((1247, 1252), (291, 291)),
    ((1253, 1258), (292, 292)),
    ((1259, 1259), (293, 293)),
    ((1260, 1265), (294, 294)),
    ((1266, 1271), (295, 295)),
    ((1272, 1272), (296, 296)),
    ((1273, 1278), (297, 297)),
    ((1279, 1279), (298, 298)),
    ((1292, 1296), (301, 301)),
    ((1298, 1303), (303, 303)),
    ((1304, 1309), (304, 304)),
    ((1310, 1315), (305, 305)),
    ((1316, 1316), (306, 306)),
    ((1317, 1322), (307, 307)),
    ((1323, 1328), (308, 308)),
    ((1329, 1329), (309, 309)),
    ((1330, 1335), (310, 310)),
    ((1336, 1336), (311, 311)),
    ((1349, 1353), (315, 315)),
    ((1355, 1360), (317, 317)),
    ((1361, 1366), (318, 318)),
    ((1367, 1372), (319, 319)),
    ((1373, 1373), (320, 320)),
    ((1374, 1379), (321, 321)),
    ((1380, 1385), (322, 322)),
    ((1386, 1386), (323, 323)),
    ((1387, 1392), (324, 324)),
    ((1393, 1393), (325, 325)),
    ((1406, 1410), (328, 328)),
    ((1412, 1417), (330, 330)),
    ((1418, 1423), (331, 331)),
    ((1424, 1429), (332, 332)),
    ((1430, 1430), (333, 333)),
    ((1431, 1436), (334, 334)),
    ((1437, 1442), (335, 335)),
    ((1443, 1443), (336, 336)),
    ((1444, 1449), (337, 337)),
    ((1450, 1450), (338, 338)),
    ((1463, 1467), (341, 341)),
    ((1469, 1474), (343, 343)),
    ((1475, 1480), (344, 344)),
    ((1481, 1486), (345, 345)),
    ((1487, 1487), (346, 346)),
    ((1488, 1493), (347, 347)),
    ((1494, 1499), (348, 348)),
    ((1500, 1500), (349, 349)),
    ((1501, 1506), (350, 350)),
    ((1507, 1507), (351, 351)),
    ((1520, 1524), (354, 354)),
    ((1526, 1531), (356, 356)),
    ((1532, 1537), (357, 357)),
    ((1538, 1543), (358, 358)),
    ((1544, 1544), (359, 359)),
    ((1545, 1550), (360, 360)),
    ((1551, 1556), (361, 361)),
    ((1557, 1557), (362, 362)),
    ((1558, 1563), (363, 363)),
    ((1564, 1564), (364, 364)),
    ((1577, 1581), (369, 369)),
    ((1583, 1588), (371, 371)),
    ((1589, 1594), (372, 372)),
    ((1595, 1600), (373, 373)),
    ((1601, 1601), (374, 374)),
    ((1602, 1607), (375, 375)),
    ((1608, 1613), (376, 376)),
    ((1614, 1614), (377, 377)),
    ((1615, 1620), (378, 378)),
    ((1621, 1621), (379, 379)),
    ((1622, 1627), (380, 380)),
    ((1628, 1628), (381, 381)),
    ((1641, 1645), (384, 384)),
    ((1647, 1652), (386, 386)),
    ((1653, 1658), (387, 387)),
    ((1659, 1664), (388, 388)),
    ((1665, 1665), (389, 389)),
    ((1666, 1671), (390, 390)),
    ((1672, 1677), (391, 391)),
    ((1678, 1678), (392, 392)),
    ((1679, 1684), (393, 393)),
    ((1685, 1685), (394, 394)),
    ((1686, 1691), (395, 395)),
    ((1692, 1692), (396, 396)),
    ((1705, 1709), (399, 399)),
    ((1711, 1716), (401, 401)),
    ((1717, 1722), (402, 402)),
    ((1723, 1728), (403, 403)),
    ((1729, 1729), (404, 404)),
    ((1730, 1735), (405, 405)),
    ((1736, 1741), (406, 406)),
    ((1742, 1742), (407, 407)),
    ((1743, 1748), (408, 408)),
    ((1749, 1749), (409, 409)),
    ((1750, 1755), (410, 410)),
    ((1756, 1756), (411, 411)),
    ((1769, 1773), (414, 414)),
    ((1775, 1780), (416, 416)),
    ((1781, 1786), (417, 417)),
    ((1787, 1792), (418, 418)),
    ((1793, 1793), (419, 419)),
    ((1794, 1799), (420, 420)),
    ((1800, 1805), (421, 421)),
    ((1806, 1806), (422, 422)),
    ((1807, 1812), (423, 423)),
    ((1813, 1813), (424, 424)),
    ((1814, 1819), (425, 425)),
    ((1820, 1820), (426, 426)),
    ((1833, 1837), (429, 429)),
    ((1839, 1844), (431, 431)),
    ((1845, 1850), (432, 432)),
    ((1851, 1856), (433, 433)),
    ((1857, 1857), (434, 434)),
    ((1858, 1863), (435, 435)),
    ((1864, 1869), (436, 436)),
    ((1870, 1870), (437, 437)),
    ((1871, 1876), (438, 438)),
    ((1877, 1877), (439, 439)),
    ((1878, 1883), (440, 440)),
    ((1884, 1884), (441, 441)),
    ((1897, 1901), (444, 444)),
    ((1903, 1908), (446, 446)),
    ((1909, 1914), (447, 447)),
    ((1915, 1920), (448, 448)),
    ((1921, 1921), (449, 449)),
    ((1922, 1927), (450, 450)),
    ((1928, 1933), (451, 451)),
    ((1934, 1934), (452, 452)),
    ((1935, 1940), (453, 453)),
    ((1941, 1941), (454, 454)),
    ((1942, 1947), (455, 455)),
    ((1948, 1948), (456, 456)),
    ((1961, 1965), (459, 459)),
    ((1967, 1972), (461, 461)),
    ((1973, 1978), (462, 462)),
    ((1979, 1984), (463, 463)),
    ((1985, 1985), (464, 464)),
    ((1986, 1991), (465, 465)),
    ((1992, 1997), (466, 466)),
    ((1998, 1998), (467, 467)),
    ((1999, 2004), (468, 468)),
    ((2005, 2005), (469, 469)),
    ((2006, 2011), (470, 470)),
    ((2012, 2012), (471, 471)),
    ((2025, 2029), (475, 475)),
    ((2031, 2036), (477, 477)),
    ((2037, 2042), (478, 478)),
    ((2043, 2048), (479, 479)),
    ((2049, 2049), (480, 480)),
    ((2050, 2055), (481, 481)),
    ((2056, 2061), (482, 482)),
    ((2062, 2062), (483, 483)),
    ((2063, 2068), (484, 484)),
    ((2069, 2069), (485, 485)),
    ((2070, 2075), (486, 486)),
    ((2076, 2076), (487, 487)),
    ((2089, 2093), (491, 491)),
    ((2095, 2100), (493, 493)),
    ((2101, 2106), (494, 494)),
    ((2107, 2112), (495, 495)),
    ((2113, 2113), (496, 496)),
    ((2114, 2119), (497, 497)),
    ((2120, 2125), (498, 498)),
    ((2126, 2126), (499, 499)),
    ((2127, 2132), (500, 500)),
    ((2133, 2133), (501, 501)),
    ((2134, 2139), (502, 502)),
    ((2140, 2140), (503, 503)),
)
